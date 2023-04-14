#!/usr/bin/node


const [primer_palabra] = process.argv.slice(2)
const [segunda_palabra] = process.argv.slice(3)


if (primer_palabra + segunda_palabra) {
	console.log(primer_palabra + " is " + segunda_palabra)
} else{
	console.log("undefined is undefined")
}
