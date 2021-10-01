$('#button').on('click', function () {
    console.log('button clicked');
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/api/customers/register/",
        data: $('#form').serialize(),

        success: function (data) {
            console.log('Im in success!');
            console.log(data);
            location.href = data.link
        },
        error: function () {
            console.log('ERROR!!!');
            console.log(this.data);
        }
    })
})