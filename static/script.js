function cap() {
    var alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V'
        , 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '%', '^', '&', '*', '+'];
    var a = alpha[Math.floor(Math.random() * 71)];
    var b = alpha[Math.floor(Math.random() * 71)];
    var c = alpha[Math.floor(Math.random() * 71)];
    var d = alpha[Math.floor(Math.random() * 71)];
    var e = alpha[Math.floor(Math.random() * 71)];
    var f = alpha[Math.floor(Math.random() * 71)];

    var final = a + b + c + d + e + f;
    document.getElementById("capt").value = final;
}
function validcap() {
    var stg1 = document.getElementById('capt').value;
    var stg2 = document.getElementById('textinput').value;
    if (stg1 == stg2) {
        alert("Form is Submitted Succesfully");
        return true;
    }
    else {
        alert("Please Enter Valid Captcha");
        return false;
    }

}

(function(endTime){
    endTime*=1000;
    endTime+=new Date().getTime();

    (function timerSync() {

        var diff = new Date(endTime - new Date().getTime());

        var timer=document.getElementById('countdown');

        if(diff<=0)return timerEnd(timer);

        timer.innerHTML =
        	doubleDigits(diff.getUTCHours())
        	+ ':' +
        	doubleDigits(diff.getUTCMinutes())
            + ':' +
        	doubleDigits(diff.getUTCSeconds())
        ;
        // recursion
        setTimeout(timerSync,1000);
    })();
	function timerEnd(timer) {
        timer.innerHTML='Timer has stopped now';
    }

    function doubleDigits(number) {
    	return number<10
        	? '0'+number
        	: number
        ;
    }
})(
    (0 * 0)+ (3 * 60) + (00)
);