$(function(){	
	$('#myfile').change(function(e){

		var file = e.target.files[0];
		var reader = new FileReader();

		//2D�R���e�L�X�g�̃I�u�W�F�N�g�𐶐�����
		var cvs = document.getElementById('cvs1');
		var ctx = cvs.getContext('2d');

		//�摜�łȂ��ꍇ�͏����I��
		if(file.type.indexOf("image") < 0){
			return false;
		}

		//�A�b�v���[�h�����摜��ݒ肷��
		reader.onload = (function(file){
			return function(e){
				var img = new Image();
				img.src = e.target.result;
				img.onload = function() {
					ctx.drawImage(img, 0, 0, 224, 224);
				}
			};
		})(file);
		reader.readAsDataURL(file);
	});
});
function callPostMethod() {
		var data = {};
		var cvs = document.getElementById('cvs1');

		$.ajax(
			{ 
				url:"/api/fish-classification",
				type: "POST",
				data:JSON.stringify(cvs.toDataURL('image/jpeg').split('base64,')[1]),
				dataType:'json',
				contentType:'application/json'
			})
		.then(function (data) {
			$("#result").append("<p>Name: " + data["result"]["0"]["name"] + " confidence: " +   data["result"]["0"]["confidence"] + "</p></br>");
			$("#result").append("<p>Name: " + data["result"]["1"]["name"] + " confidence: " +   data["result"]["1"]["confidence"] + "</p></br>");
			$("#result").append("<p>Name: " + data["result"]["2"]["name"] + " confidence: " +   data["result"]["2"]["confidence"] + "</p></br>");
		}, function (e) {
				alert("error: " + e);
		});
}