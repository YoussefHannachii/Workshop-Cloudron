const fs = require('fs');

// Read the file content
const fileContent = fs.readFileSync('/docker-entrypoint-initdb.d/CI-CD_Project.article.json', 'utf8');

// Parse the JSON data
const jsonData = JSON.parse(fileContent);

// Access the database and collection
const db = db.getSiblingDB('CI-CD_Project');  // Make sure this is the correct database name
const collection = db.getCollection('article');  // Make sure this is the correct collection name

// Insert the data into the collection
collection.insertMany(jsonData);

print('Data has been inserted successfully');
