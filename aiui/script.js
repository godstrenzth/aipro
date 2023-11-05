function submitForm(data1, data2, data3, data4, data5, data6, data7) {
    event.preventDefault();
    let end_point_url = "http://127.0.0.1:8080/api/product"

    //parseInt
    data1 = parseFloat(data1);
    data2 = parseFloat(data2);
    data3 = parseFloat(data3);
    data4 = parseFloat(data4);
    data5 = parseFloat(data5);
    data6 = parseFloat(data6);
    data7 = parseFloat(data7);

    const data = {
        data: [data1, data2, data3, data4, data5, data6, data7]
    };
    
    //console.log(JSON.stringify(data));
    fetch(end_point_url, {
        method: "POST",
        body: JSON.stringify(data),
        headers: { "Content-type": "application/json" }
        
    })
    .then((response) => response.json())
    .then((json) =>{
        // Display the result in the 'result' div
        document.getElementById("result").innerHTML = JSON.stringify(json);
    })// console.log(JSON.stringify(json)));
    //console.log(json);
}
