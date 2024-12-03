function createStatutesGoogleSheetFromDocx() {
  // ID du fichier .docx contenant les statuts
  var fileId = 'ID_DE_VOTRE_FICHIER_DOCX'; // Remplacez par l'ID de votre fichier .docx

  // Lire le contenu du fichier .docx
  var file = DriveApp.getFileById(fileId);
  var blob = file.getBlob();
  var docx = Docx.load(blob);

  // Créer un nouveau document Google Sheets
  var spreadsheet = SpreadsheetApp.create('Statuts SAS');
  var sheet = spreadsheet.getActiveSheet();

  // Ajouter les en-têtes de colonnes
  sheet.appendRow(['Chapitre', 'Sous-chapitre', 'Article']);

  // Variables pour suivre les chapitres, sous-chapitres et articles
  var currentChapter = '';
  var currentSubChapter = '';
  var currentArticle = '';

  // Lire le contenu du .docx
  var paragraphs = docx.getParagraphs();
  for (var i = 0; i < paragraphs.length; i++) {
    var paragraph = paragraphs[i];
    var text = paragraph.getText().trim();
    var style = paragraph.getStyle();

    if (style === 'Heading1') {
      currentChapter = text;
      currentSubChapter = '';
      currentArticle = '';
    } else if (style === 'Heading2') {
      currentSubChapter = text;
      currentArticle = '';
    } else if (style === 'Heading3') {
      currentArticle = text;
      sheet.appendRow([currentChapter, currentSubChapter, currentArticle]);
    } else if (text.startsWith('Annexe')) {
      // Créer un nouvel onglet pour chaque annexe
      var annexeName = text.split(':')[1].trim();
      var annexeSheet = spreadsheet.insertSheet(annexeName);
      i++; // Passer à la ligne suivante pour le contenu de l'annexe
      while (i < paragraphs.length && !paragraphs[i].getText().startsWith('Annexe')) {
        annexeSheet.appendRow([paragraphs[i].getText().trim()]);
        i++;
      }
      i--; // Revenir à la ligne précédente pour continuer la boucle
    }
  }

  // Enregistrer l'URL du document
  var url = spreadsheet.getUrl();
  Logger.log('Le document Google Sheets a été créé : ' + url);
}
