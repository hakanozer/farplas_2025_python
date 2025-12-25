// form gönderildiğini anla
$('#loginForm').submit(function (e) { 
    e.preventDefault();
    // dataları yakala
    const email = $('#email').val()
    const password = $('#password').val()

    // servise datayı hazırla
    const sendObj = {
        email: email,
        password: password
    }

    // servis url hazırla
    const url = 'https://jsonbulut.com/api/auth/login'

    // servis call
    // service url üzerinden dataları gönder
    $.ajax({
        type: "POST",
        url: url,
        data: sendObj,
        success: function (response) {
            const dt = response
            const token = dt.data.access_token
            const name = dt.data.user.name
            // dataları sakla
            localStorage.setItem('token', token)
            localStorage.setItem('name', name)
            // sayfayı yönlendir
            window.location.href = 'products.html'
        },
        error: function (err) {
            alert('Email or Password fail')
        }
    });


});