$('#button').on('click', function () {
    console.log('button clicked');
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/api/customers/forgetpassword/",
        data: $('#form').serialize(),

        success: function (data) {
            console.log('Im in success!');
            console.log(data);
            location.href = data.link
        },
        error: function (data) {
            console.log('ERROR!!!');
            location.href = this.url

        }
    })
})