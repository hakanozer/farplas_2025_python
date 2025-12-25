// sayfa yüklendiğinde otomatik olarak çalıştır
$(document).ready(function () {
    const url = 'https://jsonbulut.com/api/products?page=1&per_page=10'
    $.ajax({
        type: "GET",
        url: url,
        success: function (response) {
            const arr = response.data
            var rows = ''
            for (let i = 0; i < arr.length; i++) {
                const item = arr[i];
                rows += `<tr>
                <th scope="row">${item.id}</th>
                <td><img src='${item.images[0]}' width=100 /></td>
                <td>${item.title}</td>
                <td>${item.price}</td>
                <td>${item.category}</td>
            </tr>` 
            }
            $('#tbody').html(rows)
        }
    });
});