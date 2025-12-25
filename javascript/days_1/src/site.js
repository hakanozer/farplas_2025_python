// tek satırlı açıklama satırı
/*
 çok satırlı açıklama satılar
*/

// değişkenler
// var , const
// var -> değişime uygun 
// string ifadelerde '', yada "" arasında fark yoktur
var username = 'Ali'
var surname = "Bilmem"
var concat = username + surname
var sumConcat = `${username} ${surname}`

var num1 = 100
var num2 = 10.5
var sum = num1 + num2
console.log("Sum :", sum)

// karar kontrol yapıları için kullanılır - true - false
var status = false

// object type
var item = {
    id: 10,
    name: 'Ali',
    surname: 'Bilmem',
    address: [
        {title: 'Yazlık', addresDetail: 'Muğla Addres', no: 10},
        {title: 'İş', addresDetail: 'İstanbul Addres', no: 15},
    ]
}
// object içindeki değerler (.) ile ayrılır.
console.log(item.name)
console.log(item.address[0].title)
// dizi kaç elemandan oluşuyor
console.log(item.address.length)

// tüm adreslere ulaş
// for - loop
for (let i = 0; i < item.address.length; i++) {
    var singleAddress = item.address[i]
    if (singleAddress.title == 'Yazlık') {
        console.log("Tatil time!!!")
    }
}

// sendBtn id li butona tıklandığında
// butonun içeriğini değiştir
var sendBtn = document.getElementById('sendBtn')
var name = document.getElementById('name')
var surname = document.getElementById('surname')
var email = document.getElementById('email')
var sicil = document.getElementById('sicil')

sendBtn.onclick = function() {
    sendBtn.innerHTML = 'Gönderildi'
    sendBtn.style.backgroundColor = 'red'

    const nameValue = name.value
    const surnameValue = surname.value
    const emailValue = email.value
    const sicilValue = sicil.value

    if (nameValue == '' || surnameValue == '') {
        alert('Lütfen tüm alanları doldurunuz')
    }else {
        alert(`Sayın ${nameValue} ${surnameValue}, kaydınız başarıyla alınmıştır.`)
    }

}

