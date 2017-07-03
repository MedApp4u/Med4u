$(".clickable").click(function(){
    // $("#div1").load("demo_test.txt", function(responseTxt, statusTxt, xhr){
    //     if(statusTxt == "success")
    //         alert("External content loaded successfully!");
    //     if(statusTxt == "error")
    //         alert("Error: " + xhr.status + ": " + xhr.statusText);
    // });

    alert("Medicine has already been added to My Medicines!");
});

function submitForm(){
	$('#hidden-medicine-form').submit();
	$('#hidden-doctor-form').submit();
}