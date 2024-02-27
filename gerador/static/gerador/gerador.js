function refresh() {
    document.addEventListener('DOMContentLoaded', function(){
        numbers = document.querySelector(".numbers")
        numbers.innerHTML.load(numbers)
    })
}