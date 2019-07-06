// We can take importing d3 as an example
// this is taken from the d3 readme file
// if we would like to import something speicific from 
// d3, we do the following: 


import {scaleLinear} from "d3-scale";

// if we would like to import everything 
// to a namespace:
import * as d3 from "d3"

// worth noting that the libraries need to be
// included by linking to them in <head> of the .html
// TODO: exploring server-side import, or ny using node.js