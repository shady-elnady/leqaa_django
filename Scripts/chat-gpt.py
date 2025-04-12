from typing import List

from langchain_community.agent_toolkits import FileManagementToolkit
from langchain_community.tools import ShellTool
from langchain_core.messages import SystemMessage
from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_openai import ChatOpenAI

from config.settings import OPENAI_API_KEY
from utils.translation.prompts import SYSTEM_PROMPT, MAIN_PROMPT

# LangChain Tools
tools = FileManagementToolkit(
    root_dir="../../Assets/locales/",
    selected_tools=["read_file", "write_file", "list_directory", "file_delete"],
).get_tools()
read_tool, write_tool, list_tool, delete_tool = tools
shell_tool = ShellTool()

# OpenAI model
model_name = "gpt-4o-mini"
model = ChatOpenAI(
    model_name=model_name,
    temperature=0.0,
    openai_api_key=OPENAI_API_KEY,
    max_retries=1,
    model_kwargs={},
)


def main():
    languages = get_languages()
    delete_old_messages_files(languages)
    create_new_messages_files(languages)
    translate_files(languages)

    print("All steps done!")


def translate_files(languages: List[str]):
    # Translate all languages and write to the files
    print("\n====================================\nTranslating all languages")
    for lang in languages:
        content = read_tool.invoke({"file_path": f"{lang}/LC_MESSAGES/django.po"})
        translation = translate(content, lang)
        write_tool.invoke(
            {"file_path": f"{lang}/LC_MESSAGES/django.po", "text": translation}
        )
    print("====================================")


def create_new_messages_files(languages: List[str]):
    # Make new messages files
    print("\n====================================\nCreating new messages files")
    print(
        shell_tool.run(
            {"commands": ["cd ../../ && python manage.py makemessages --all"]}
        )
    )
    print("====================================")


def delete_old_messages_files(languages: List[str]):
    print(f"\n====================================\nDeleting old messages files")
    # Delete messages files
    for lang in languages:
        filename = f"{lang}/LC_MESSAGES/django.po"
        print(f" Deleting file: {filename}")
        delete_tool.invoke({"file_path": f"{lang}/LC_MESSAGES/django.po"})
    print("====================================")


def translate(content: str, target_language: str) -> str:
    print(f" Translating to {target_language}")
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessagePromptTemplate.from_template(template=MAIN_PROMPT),
        ]
    )
    chain_tmp = prompt | model
    chain = chain_tmp.with_config({"tags": ["locale_translation"]})
    input = {"language": target_language, "file_content": content}
    response = chain.invoke(input)
    return f"# Auto translated with {model_name}\n{response.content}"


def get_languages() -> List[str]:
    dirs = list_tool.invoke({"dir_path": ""})
    languages = [name for name in dirs.split() if name != "README.rst" and name != "en"]
    return languages


if __name__ == "__main__":
    main()
