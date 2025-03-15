const locales = [
  "en-GB",
  "ar-SA",
  "zh-CN",
  "de-DE",
  "es-ES",
  "fr-FR",
  "hi-IN",
  "it-IT",
  "in-ID",
  "ja-JP",
  "ko-KR",
  "nl-NL",
  "no-NO",
  "pl-PL",
  "pt-BR",
  "sv-SE",
  "fi-FI",
  "th-TH",
  "tr-TR",
  "uk-UA",
  "vi-VN",
  "ru-RU",
  "he-IL",
];

jQuery.ajax({
  url: "url_pattern_in_urls_py_file/",
  type: "POST",
  contentType: "application/json; charset=UTF-8",
  data: JSON.stringify({ updated_data: your_data_val }),
  dataType: "json",
  success: function (return_data) {
    //success body
  },
});

function getFlagSrc(countryCode) {
  return /^[A-Z]{2}$/.test(countryCode)
    ? `https://flagsapi.com/${countryCode.toUpperCase()}/shiny/64.png`
    : "";
}

const dropdownBtn = document.getElementById("dropdown-btn");
const dropdownContent = document.getElementById("dropdown-content");

function setSelectedLocale(locale) {
  const intlLocale = new Intl.Locale(locale);
  const langName = new Intl.DisplayNames([locale], {
    type: "language",
  }).of(intlLocale.language);

  dropdownContent.innerHTML = "";

  const otherLocales = locales.filter((loc) => loc !== locale);
  otherLocales.forEach((otherLocale) => {
    const otherIntlLocale = new Intl.Locale(otherLocale);
    const otherLangName = new Intl.DisplayNames([otherLocale], {
      type: "language",
    }).of(otherIntlLocale.language);

    const listEl = document.createElement("li");
    listEl.innerHTML = `${otherLangName}<img src="${getFlagSrc(
      otherIntlLocale.region
    )}" />`;
    listEl.value = otherLocale;
    listEl.addEventListener("mousedown", function () {
      setSelectedLocale(otherLocale);
      console.log(otherLocale);
    });
    dropdownContent.appendChild(listEl);
  });

  dropdownBtn.innerHTML = `<img src="${getFlagSrc(
    intlLocale.region
  )}" />${langName}<span class="arrow-down"></span>`;
}

setSelectedLocale(locales[0]);
const browserLang = new Intl.Locale(navigator.language).language;
console.log(navigator.language);
for (const locale of locales) {
  const localeLang = new Intl.Locale(locale).language;
  if (localeLang === browserLang) {
    setSelectedLocale(locale);
  }
}
