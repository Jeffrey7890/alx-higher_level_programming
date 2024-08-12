$(document).ready(function () {
  function fetchTranslation () {
    const languageCode = $('#language_code').val();

    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function (data) {
      $('#hello').text(data.hello);
    }).fail(function () {
      $('#hello').text('Error: Could not fetch translation.');
    });
  }

  $('#btn_translate').click(function () {
    fetchTranslation();
  });

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
