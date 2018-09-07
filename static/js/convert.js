$(document).ready(function(){
	$('form').on('submit', function(event){
		$.ajax({
			type: "POST",
			url: "/convert",
			success: function(response){
				console.log(response);
			},
			data: {
				myinput: $('.is-active > div.source >label').text(),
				myoutput: $('.is-active > div.destination >label').text(),
				source: $('.is-active > div.source > textarea').val()
			}
		})

		.done(function(data){
			if(data.error){
				//Do Something
			}
			else {
				console.log("ehlo");
				$('.is-active > div.destination > textarea').val(data.output).show();
			}
		});
		event.preventDefault();
	});
});
