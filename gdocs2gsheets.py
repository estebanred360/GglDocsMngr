function createGoogleDocFromGoogleSheet() {
  // ID du document Google Sheets
  var sheetId = 'ID_DE_VOTRE_DOCUMENT_GOOGLE_SHEETS'; // Remplacez par l'ID de votre document Google Sheets

  // Ouvrir le document Google Sheets
  var spreadsheet = SpreadsheetApp.openById(sheetId);
  var sheets = spreadsheet.getSheets();

  // Créer un nouveau document Google Docs
  var doc = DocumentApp.create('Statuts SAS');
  var body = doc.getBody();

  // Parcourir chaque onglet du document Google Sheets
  for (var i = 0; i < sheets.length; i++) {
    var sheet = sheets[i];
    var sheetName = sheet.getName();
    var data = sheet.getDataRange().getValues();

    // Ajouter un titre pour l'annexe si ce n'est pas l'onglet principal
    if (sheetName.toLowerCase().includes('annexe')) {
      body.appendParagraph(sheetName).setHeading(DocumentApp.ParagraphHeading.HEADING1);
    }

    // Parcourir les lignes du document Google Sheets
    for (var j = 1; j < data.length; j++) {
      var row = data[j];
      var chapter = row[0];
      var subChapter = row[1];
      var article = row[2];

      if (chapter) {
        body.appendParagraph(chapter).setHeading(DocumentApp.ParagraphHeading.HEADING1);
      }
      if (subChapter) {
        body.appendParagraph(subChapter).setHeading(DocumentApp.ParagraphHeading.HEADING2);
      }
      if (article) {
        body.appendParagraph(article).setHeading(DocumentApp.ParagraphHeading.HEADING3);
      }
    }

    // Ajouter une page de séparation entre les annexes
    if (i < sheets.length - 1) {
      body.appendPageBreak();
    }
  }

  // Enregistrer l'URL du document Google Docs
  var url = doc.getUrl();
  Logger.log('Le document Google Docs a été créé : ' + url);
}
