//check off specific todo by clicking
$("ul").on("click","li",function(){
//the reason for the use of this is syntax is becasue when the 
//page initially loads it will account for li's that dont exist then but 
//exist when we add them. Hence we select in the $() a tag that exists
//and use on with "li" as an argument to account for the li's to be added.
//same concept for the span, as every new li also has a span in it.
	// //if grey then make it black and remove the line through
	// if($(this).css("color") === "rgb(128, 128, 128)"){
	// 	$(this).css({
	// 		color:"black",
	// 		textDecoration:"none"
	// 	});
	// }
	// else{
	// 	$(this).css({
	// 	color:"gray",
	// 	textDecoration: "line-through"
	// });

	// }
	//OR
	$(this).toggleClass("completed");
});

//click on x to delete todo
$("ul").on("click","span",function(event){
	$(this).parent().fadeOut(500,function(){
			$(this).remove();//we put this in the fadeout callback function as we want to fade the element and then remove the html element!
			//if this code was outside it would not wait for the element to fade! IMP.
		});//the this in the second time refers to the parent straight away.
		
	event.stopPropagation();
	//concept of preventing event bubbling: this prevents the event from passing on to parent elements as technically span
	//is a part of li. so technically the span event will be triggered first and since span is a part of li,li click event 
	//will be triggered as well. IMP.
});

$("input[type ='text']").keypress(function(event){
	if(event.which === 13){//to see if enter key is pressed
		var todo = $(this).val();//retrieve the thing entered by the user
		$(this).val('');//make the input box blank again
		//create the new li-html element using append
		$("ul").append("<li><span><i class='fa fa-trash'></i></span> "+ todo +"</li>");
	}
});

$(".fa-plus").click(function(){//so that trash can fades in and out
	$("input[type ='text']").fadeToggle();

});