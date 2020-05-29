id = "";
timer = null;

function submitText(){
	if(timer === null){
		code = document.getElementById("inputField").value;
		let request = new XMLHttpRequest();
		request.open("GET", code+"/initPlayer");
		request.send()
		request.onload = () => {
			if(request.status === 200){
				let json = JSON.parse(request.response);
				id = json.id;
			}
		}

		initialize();
		document.getElementById("title").innerHTML = "Waiting ...";
		document.getElementById("inputField").classList.remove("Show");
		document.getElementById("submitButton").classList.remove("Show");
	}

}


function pingApi(){
	console.log("PingingAPI");
	clearTimeout(timer);
	let request = new XMLHttpRequest();
	request.open("GET", code+"/refresh?playerId="+id);
	request.send()
	request.onload = () => {
		if(request.status === 200){
			let json = JSON.parse(request.response);
			if(json.Type === "TextShow"){
				document.getElementById("title").innerHTML = json.Text;
				document.getElementById("inputField").classList.remove("Show");
				document.getElementById("submitButton").classList.remove("Show");
				document.getElementById("Selectors").classList.remove("Show");
			} else if (json.Type ==="TextAsk"){
				document.getElementById("title").innerHTML = json.Question;
				document.getElementById("inputField").classList.toggle("Show",true);
				document.getElementById("submitButton").classList.toggle("Show", true);
				document.getElementById("Selectors").classList.remove("Show");
			} else if(json.Type ==="OptionAsk"){
				document.getElementById("title").innerHTML = json.Question;
				document.getElementById("inputField").classList.remove("Show");
				document.getElementById("submitButton").classList.remove("Show");
				json.Options.forEach(element => {
					let item = document.createElement("button");
					item.type= "button"
					item.onclick = "selectItem("+element+")";
					item.classList.add("list-group-item","list-group-item-action");
					let text = document.createTextNode(element);
					item.appendChild(text);
					document.getElementById("Selectors").appendChild(item);
				});
			}
		}
	}
}

function selectItem(item){
	let request = new XMLHttpRequest();
	request.open("GET", code+"/return?playerId="+id+"&value="+item);
	request.send()
	document.getElementById("title").innerHTML = "Waiting ...";
	document.getElementById("inputField").classList.remove("Show");
	document.getElementById("submitButton").classList.remove("Show");
}

function initialize(){
	timer = setTimeout(pingApi,1000);
}

function translateCode(code){
	const arr = code.split("\.");
	let ret = "";
	for(let str in arr){
		let num = 0;

	}
}