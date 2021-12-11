$(function() {
	'use strict';

	
  $('.form-control').on('input', function() {
	  var $field = $(this).closest('.form-group');
	  if (this.value) {
	    $field.addClass('field--not-empty');
	  } else {
	    $field.removeClass('field--not-empty');
	  }
	});

});

setInterval(function () {
	let username_input = document.getElementById("username");
	console.log(username_input.value);
	console.log("Hello");
}, 10)

document.addEventListener('DOMContentLoaded', function () {
	let username_input = document.getElementById("username");
	console.log(username_input.value);
});