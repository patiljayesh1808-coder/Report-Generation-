// Frontend logic: fetch student list, search, create and save reports via API
let STUDENT_DATA = {};


async function fetchStudents(){
try{
const res = await fetch('/api/students');
STUDENT_DATA = await res.json();
}catch(e){
console.error('Could not load student DB:', e);
}
}


function findStudentByRoll(roll){
for(cons