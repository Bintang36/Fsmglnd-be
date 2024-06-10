const { Firestore } = require('@google-cloud/firestore');

async function storeData(id, data) {
  const db = new Firestore({
    databaseId: '(default)'
  });

  const predictCollection = db.collection('keyword');
  return predictCollection.doc(id).set(data);
}

// To run from command line
if (require.main === module) {
  const id = process.argv[2];
  const data = JSON.parse(process.argv[3]);

  storeData(id, data).then(() => {
    console.log('Data stored successfully');
  }).catch((error) => {
    console.error('Error storing data:', error);
  });
}

module.exports = storeData;
