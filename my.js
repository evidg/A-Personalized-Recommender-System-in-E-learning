$(document).ready(function(){
	$("#form1").submit(function(){
		$.post("/signup2", $("#form1").serialize(), function(res)
			{
				js=res;
				if(js.err==1)
				{
				$("#err").html("<div class=\"alert alert-danger\">This username exists</div>");
				}
				else
				{
				$("#err").html("<div class=\"alert alert-success\">Your data saved!</div>");
				}
			}	
		);
	
		event.preventDefault();	
	});
	
	
	$("#form5").submit(function(){
	event.preventDefault();
		$.post("/updateprofile", $("#form5").serialize(), function(res)
			{
				js=res;
				if(js.err==1)
				{
				$("#err").html("<div class=\"alert alert-danger\">This username exists</div>");
				}
				else
				{
				$("#err").html("<div class=\"alert alert-success\">Your data saved!</div>");
				}
			}	
		
		);
		
		event.preventDefault();	
		
	});
	
	
$("#form6").submit(function(){
	event.preventDefault();
		$.post("/addcat", $("#form6").serialize(), function(res)
			{
				getCategories();
			}		
		);
	
		event.preventDefault();
	
	});
	

$("#form10").submit(function(){
	event.preventDefault();
		$.post("/ins2", $("#form10").serialize(), function(res)
			{
				js=res;
				if(js.err==1)
				{
				
				$("#err").html("<div class=\"alert alert-danger\">Error.Your data did not saved</div>");
				}
				else
				{
				$("#form10").hide(1000);
				$("#err").html("<div class=\"alert alert-success\">Your data saved!</div>");
				}
			}				
		);		
	});
	

$("#form15").submit(function(){
	event.preventDefault();
		$.post("/updateprofile", $("#form15").serialize(), function(res)
			{
				js=res;
				if(js.err==1)
				{
				
				$("#err").html("<div class=\"alert alert-danger\">Error.Your data did not saved</div>");
				}
				else
				{
				
				$("#err").html("<div class=\"alert alert-success\">Your data saved!</div>");
				}
			}				
		);
		});
		

$("#form16").submit(function(){
	event.preventDefault();
		$.post("/updateuser", $("#form16").serialize(), function(res)
			{
				js=res;
				if(js.err==1)
				{
				
				$("#err").html("<div class=\"alert alert-danger\">Error.Your data did not saved</div>");
				}
				else
				{
				
				$("#err").html("<div class=\"alert alert-success\">Your data saved!</div>");
				}
			}				
		);				
	});	
});


function getusers()
{

	$.get("/getusers",function (res){
		html="<table class=table >";
		html+="<thead><tr><th>id</th><th>Username</th><th>Fullname</th><th>Sex</th><th>Speciality</th><th>Type</th><th>YearBirth</th><th></th></thead><tbody id=usr1>";
		for (var i=0;i<res.length;i++)
		{
			html+="<tr><td>"+res[i].id+"</td><td>"+res[i].username+"</td><td>"+res[i].fullname+"</td>";
			html+="<td>"+res[i].sex+"</td><td>"+res[i].speciality+"</td><td>"+res[i].type+"</td>";
			html+="<td>"+res[i].yearbirth+"</td><td><a href='edituser/"+res[i].id+"'><span class='glyphicon glyphicon-edit'></span></a></td></tr>";
			
		}
		html+="</tbody></table >";
		$("#users1").html(html);
		
		$("#searchusr").keyup(
		function (){
			tr=$("#usr1 tr");
			v=$("#searchusr").val();
			for (i=0;i<tr.length;i++)
				{
					if($(tr[i]).text().indexOf(v)>-1)
					{
					$(tr[i]).show();
					}
					else
					{
					$(tr[i]).hide();
					}
					
				}				
		});	
	});	
}


function update()
{
	$.get("/getProfile",function (res){

		$("#username").val(res[2]);
		$("#pwd").val(res[3]);
		$("#fname").val(res[1]);
		$("#year1").val(res[7]);
		$("#sex").val(res[4]).change();
		$("#sp").val(res[6]).change();
		$("#role").html(res[5]);
		console.log(res);
	});
}


function edituserjs(id1)
{
	$.get("/edituserjs/"+id1,function (res){

		$("#username").val(res[2]);
		$("#pwd").val(res[3]);
		$("#fname").val(res[1]);
		$("#year1").val(res[7]);
		$("#sex").val(res[4]).change();
		$("#sp").val(res[6]).change();
		$("#role").val(res[5]).change();
		console.log(res);
	});
}


function deletecat(id)
{
	$.get("/delcat/"+id,function(res){getCategories();});	
}


function savecat(id)
{
n=$("#les"+id).val();
$.get("/savecat/"+id+"/"+n,function(res){getCategories();});
}


function getCategories()
{

	$.get("/getcats",function (res){
		html="";
		
		for (var i=0;i<res.length;i++)
		{
			html+="<div style='text-align:center'><input type=text id=les"+res[i].id+
			" value='"+res[i].title+"' style='border:none; width:200px;'> <a onclick='savecat("+res[i].id+")'><span class='glyphicon glyphicon-floppy-disk'></span></a> <a onclick='deletecat("+res[i].id+")'><span class='glyphicon glyphicon-trash'></a></span></div>";
		
		
		}
		
		$("#cat1").html(html);
		
	});
}


function getCategories2()
{

	$.get("/getcats",function (res){
		html="<div style='text-align:center'><h2>Choose Lesson</h2>";
		
		for (var i=0;i<res.length;i++)
		{
			html+="<h3><a href='/recom21/"+res[i].id+"'>"+res[i].title+"</a></h3>";
			
		}
		html+="</div>";
		$("#cat1").html(html);
			
	});
}


var ch=0;
function seteval(id)
{
	if(ch==1){
	v=$("#val_"+id).val();
	
	$.get("/setval/"+id+"/"+v,function(res){});
	}
}


function getRecom(id)
{

	$.get("/getrecom/"+id,function (res){
	
	html="";
	for (i=0;i<res.length;i++)
	{
		html="<div class='container data' style='border:1px solid gray; border-radius:10px; padding:15px; margin-top:10px;'><h3>"+res[i].title+"</h3><i>User: "+res[i].user+"</i>";
		
		html+="<p>"+res[i].perigrafi+"</p>";
		
		
		html+="<p><a href='"+res[i].link+"' target=_blank onclick='putViews("+res[i].id+")'>"+res[i].link+"</a></p>";		
		html+="<div class='row'><div class=col-md-6>Your Evaluation:<select id='val_"+res[i].id+"' onchange='seteval("+res[i].id+")'>";
		html+="<option value=-1>-Evaluation-</option>";
		html+="<option value=1>Strongly Bad</option>";
		html+="<option value=2>Bad</option>";
		html+="<option value=3>Neutral</option>";
		html+="<option value=4>Good</option>";
		html+="<option value=5>Very Good</option>";
		html+="</select></div><div class=col-md-6>Similarity:"+(1-res[i].dist).toFixed(2)+" | Average Degree: <span id='av_"+res[i].id+"'></span></div>";
		
		html+="</div></div>";
		
		$("#cat1").append(html);
				
	}	
	
	$.get("/getval",function(res){
		for (i=0;i<res.length;i++)	
			$("#val_"+res[i].id).val(res[i].d).change();
		ch=1;	
				  
		  $.get("/getval2",function(res){
			console.log(res);
			for (i=0;i<res.length;i++){	
			try{
				if(!isNaN(res[i].d)){
					
						$("#av_"+res[i].id).html(Number(res[i].d).toFixed(2));
					}
			}
					catch(e){
						
					}				
			}	
			
			});	
		}
		);	
	
	
	$("#search1").keyup(function(){
		
		var v=$("#search1").val();
		$(".data").each(function(){
			if($(this).text().toLowerCase().indexOf(v.toLowerCase())<0){
				$(this).hide();
			}
			else
			{
				$(this).show();
			}
		})	
	});
});

}


function getmyrec()
{

	$.get("/getmyrecom",function (res){
	console.log(res);
	html="";
	for (i=0;i<res.length;i++)
	{
		html="<div class='container data' style='border:1px solid gray; border-radius:10px; padding:15px; margin-top:10px;'><h3>"+res[i].title+" - Lesson:"+res[i].ltitle+"</h3>";
		
		html+="<p>"+res[i].perigrafi+"</p>";
		
		
		html+="<p><a href='"+res[i].link+"' target=_blank onclick='putViews("+res[i].id+")'>"+res[i].link+"</a></p>";		
		html+="<div class='row'><div class=col-md-6>Your Evaluation:<select id='val_"+res[i].id+"' onchange='seteval("+res[i].id+")'>";
		html+="<option value=-1>-Evaluation-</option>";
		html+="<option value=1>Strongly Bad</option>";
		html+="<option value=2>Bad</option>";
		html+="<option value=3>Neutral</option>";
		html+="<option value=4>Good</option>";
		html+="<option value=5>Very Good</option>";
		html+="</select></div>";
		
		html+="</div></div>";
		
		$("#cat1").append(html);
				
	}	
	
	$.get("/getval",function(res){
		for (i=0;i<res.length;i++)	
			$("#val_"+res[i].id).val(res[i].d).change();
			
			ch=1;
		});	
		
	$("#search1").keyup(function(){
		
		var v=$("#search1").val();
		$(".data").each(function(){
			if($(this).text().toLowerCase().indexOf(v.toLowerCase())<0){
				$(this).hide();
			}
			else
			{
				$(this).show();
			}
		})	
	});
	
	});
	
}


function putViews(id1)
{
	$.get("/putViews/"+id1,function(res){});
	
}


function putCategories()
{

	$.get("/getcats",function (res){
		html="<option>--Select Lesson--</option>";
		
		for (var i=0;i<res.length;i++)
		{
			html+="<option value='"+res[i].id+"'>"+res[i].title+"</option>";
				
		}
		
		$("#category").html(html);
			
	});
}
