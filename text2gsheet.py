function createStatutesGoogleSheet() {
  // ID du fichier texte contenant les statuts
  var fileId = 'ID_DE_VOTRE_FICHIER_TEXTE';

  // Lire le contenu du fichier texte
  var file = DriveApp.getFileById(fileId);
  var content = file.getBlob().getDataAsString();

  // Créer un nouveau document Google Sheets
  var spreadsheet = SpreadsheetApp.create('Statuts SAS');
  var sheet = spreadsheet.getActiveSheet();

  // Ajouter les en-têtes de colonnes
  sheet.appendRow(['Chapitre', 'Sous-chapitre', 'Article']);

  // Variables pour suivre les chapitres, sous-chapitres et articles
  var currentChapter = '';
  var currentSubChapter = '';
  var currentArticle = '';

  // Lire le contenu ligne par ligne
  var lines = content.split('\n');
  for (var i = 0; i < lines.length; i++) {
    var line = lines[i].trim();

    if (line.startsWith('Chapitre')) {
      currentChapter = line;
      currentSubChapter = '';
      currentArticle = '';
    } else if (line.startsWith('Sous-chapitre')) {
      currentSubChapter = line;
      currentArticle = '';
    } else if (line.startsWith('Article')) {
      currentArticle = line;
      sheet.appendRow([currentChapter, currentSubChapter, currentArticle]);
    } else if (line.startsWith('Annexe')) {
      // Créer un nouvel onglet pour chaque annexe
      var annexeName = line.split(':')[1].trim();
      var annexeSheet = spreadsheet.insertSheet(annexeName);
      i++; // Passer à la ligne suivante pour le contenu de l'annexe
      while (i < lines.length && !lines[i].startsWith('Annexe')) {
        annexeSheet.appendRow([lines[i].trim()]);
        i++;
      }
      i--; // Revenir à la ligne précédente pour continuer la boucle
    }
  }

  // Enregistrer l'URL du document
  var url = spreadsheet.getUrl();
  Logger.log('Le document Google Sheets a été créé : ' + url);
}
