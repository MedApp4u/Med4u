$(".medicine-clickable").click(function(){
    alert("Medicine already exists in your medicines!");
});

$(".doctor-clickable").click(function(){
    alert("Doctor already exists in your doctors!");
});

function submitForm(){
	$('#hidden-medicine-form').submit();
	$('#hidden-doctor-form').submit();
}