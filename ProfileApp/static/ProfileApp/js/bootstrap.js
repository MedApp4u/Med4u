$(".medicine-clickable").click(function(){
    alert("Medicine already exists in your medicines!");
});

$(".doctor-clickable").click(function(){
    alert("Doctor already exists in your doctors!");
});

$(".user-not-found").click(function(){
    alert("You need to be logged in to access this feature!");
});


function submitForm(){
	$('#hidden-medicine-form').submit();
	$('#hidden-doctor-form').submit();
}