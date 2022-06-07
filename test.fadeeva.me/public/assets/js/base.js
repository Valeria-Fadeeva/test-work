$(document).ready(function () {
	var links = document.querySelectorAll(".nav-link");

	for (i = 0; i < links.length; i++) {
		if (location.pathname == links[i].getAttribute("href")) {
			var cur = links[i].parentElement.classList.add("active");;
		}
	}

	$('.to-top').click(function (e) {
		$('html, body').animate({scrollTop: 0}, 1000);
		e.preventDefault();
	});

	$('.to-down').click(function (e) {
		$('html, body').animate({scrollTop: $(document).height() - $(window).height()}, 1000);
		e.preventDefault();
	});

    rm_card=document.querySelectorAll(".rm-card");
	if (rm_card.length != 0){
		d = new Date()

		year = d.getFullYear();
        
		month = d.getMonth()+1;
		if (month < 10) {
			month = '0' + month;
		}
        
		day = d.getDate();
        if (day < 10) {
			day = '0' + day;
		}

		ds = year + '.' + month + '.' + day;


		for (i = 0; i < rm_card.length; i++) {
			if (ds >= rm_card[i].children[2].innerText) {
				rm_card[i].children[2].parentElement.classList.add("card-active");
			} else {
				rm_card[i].children[2].parentElement.classList.add("card-deactive");
			}
		}
	}
	
	progressBar = document.querySelectorAll('.progress-bar');
	for (i = 0; i < progressBar.length; i++) {
		x_val = progressBar[i].getAttribute("aria-valuenow");
		max_val = progressBar[i].getAttribute("aria-valuemax");
		x_perc = x_val * 100 / max_val;
		progressBar[i].style.width = x_perc + "%";
		progressBar[i].style.color = "#fff";
		progressBar[i].innerText = Math.round(x_perc) + "%";
	}
})

