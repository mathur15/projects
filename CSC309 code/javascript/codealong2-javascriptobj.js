//the info we extract is json.
//JS is a functional language
//tutorial 2 about accessing objects
let data = "Som"
data = ['s1','s2','s3']

//accessing the array
console.log("One of the students are:", data[0])

//object literal
//collection of key value pairs
//any datatype can be put in including functions
data = {
	prof: 'Gonzalez',
	students: ['s1','s2','s3']
}

//displayed as an array
console.log("All students", data.students)



//introducing a new attribute in the object
data.quantity = 100

let year = "year" // could do let year = 50 as well
data[year] = 2017 //using the "year" value as a key
//can use variables in this notation
//in the dot notation, we hard code the attribute

data.do = function(){
	console.log("Hello world")
}

//to call the function in object

data.do()

//object within object
let complexData = {
	name: "Verycomplex",
	contents : data
}
//display the whole object
console.log(data)

//display complexData
console.log(complexData)

//access complexData-layered dot notation
complexData.contents.do()
console.log( "one of students",complexData.contents.students[2])

//notes about json

//JSON is built in - Javascript object notation
   //-JSON parse : long string of chars and read them as an object and create the object
   //keys are double quoted