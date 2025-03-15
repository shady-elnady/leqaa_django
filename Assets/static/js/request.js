xhr.open("GET", "{% url 'app-locale-list' %}");
xhr.send();
xhr.responseType = "json";
xhr.onload = () => {
  if (xhr.readyState == 4 && xhr.status == 200) {
    window.locales = xhr.response.results;
  } else {
    console.log(`Error: ${xhr.status}`);
  }
  setSelectedLocale(
    window.locales.find(
      (locale) =>
        locale.locale_code.toLowerCase() === `{{ LANGUAGE_CODE }}`.toLowerCase()
    )
  );
};
