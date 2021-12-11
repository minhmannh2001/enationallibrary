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

document.addEventListener('DOMContentLoaded', function () {
	let username_input = document.getElementById("username");
	if (username_input.value.length > 0) {
		field_input = document.querySelector("body > div.content > div > div > div.col-md-5.contents > div > div > form > div.form-group.first")
		field_input.classList.add("field--not-empty");
	}
});

document.addEventListener('DOMContentLoaded', function () {
	let email_input = document.getElementById("email");
	if (email_input.value.length > 0) {
		field_input = document.querySelector("body > div.content > div > div > div.col-md-5.contents > div > div > form > div.form-group.second")
		field_input.classList.add("field--not-empty");
	}
});