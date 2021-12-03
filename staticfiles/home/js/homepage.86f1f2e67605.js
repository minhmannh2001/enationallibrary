let index = 0;
let positionX = 0;
const slider = document.querySelector(".homeBanner");
const sliderMain = document.querySelector(".homeBanner-main");
let sliderItems = document.querySelectorAll(".homeBanner-item");
const dotItems = document.querySelectorAll(".homeBanner-dot-item");

let sliderItemWidth = sliderItems[0].offsetWidth;

//Auto Slide for Banner
let changeImage = function() {
    if (index >= sliderItems.length - 1) {
        index = 0;
        positionX = sliderItems[0].offsetWidth;
    } else index++;
    positionX = positionX - sliderItems[0].offsetWidth;
    sliderMain.style = `transform: translateX(${positionX}px)`;

    [... dotItems].forEach(el => el.classList.remove("active"));
    dotItems[index].classList.add("active");
}
setInterval(changeImage, 5000);

//Click to slide banner
window.addEventListener("load", function(){
    const nextBtn = document.querySelector(".homeBanner-next");
    const prevBtn = document.querySelector(".homeBanner-prev");

    const sliderLength = sliderItems.length;

    nextBtn.addEventListener("click", function(){
        handleChangSlide(1);
    });

    prevBtn.addEventListener("click", function(){
        handleChangSlide(-1);
    });

    [... dotItems].forEach(item => item.addEventListener("click", function(e) {
        [... dotItems].forEach(el => el.classList.remove("active"));
        e.target.classList.add("active");
        const slideIndex = parseInt(e.target.dataset.index);
        index = slideIndex;
        positionX = -1 * index * sliderItemWidth;
        sliderMain.style = `transform: translateX(${positionX}px)`;
    }));
    function handleChangSlide(direction) {
        if (direction == 1) {
            if (index >= sliderLength - 1) {
                index = 0;
                positionX = sliderItemWidth;
            } else index++;
            positionX = positionX - sliderItemWidth;
            sliderMain.style = `transform: translateX(${positionX}px)`;
            // console.log(index);
            // console.log(sliderItemWidth);
            // console.log(positionX);
        }
        else if (direction == -1) {
            if (index <= 0) {
                index = sliderItems.length;
                positionX = positionX - sliderItemWidth*sliderItems.length;
            } else index--;
            positionX = positionX + sliderItemWidth;
            sliderMain.style = `transform: translateX(${positionX}px)`;
            // console.log(index);
            // console.log(sliderItemWidth);
            // console.log(positionX);
        }
        [... dotItems].forEach(el => el.classList.remove("active"));
        dotItems[index].classList.add("active");
    }
});

//If resize the window, banner begins at image(index= '0')
window.addEventListener('resize', function(){
    sliderItems = document.querySelectorAll(".homeBanner-item");
    sliderItemWidth = sliderItems[0].offsetWidth;

    index = 0;
    positionX = 0;
    sliderMain.style = `transform: translateX(${positionX}px)`;
    [... dotItems].forEach(el => el.classList.remove("active"));
    dotItems[index].classList.add("active");

    // console.log(index);
    // console.log(sliderItemWidth);
});

//Script to Top Borrow Slider
window.addEventListener("load", function(){
    const slider = document.querySelector(".tbBookList");
    const sliderMain = document.querySelector(".tbSlick-track");
    const sliderItems = document.querySelectorAll(".tbSlick-slide");
    const nextBtn = document.querySelector(".tbSlider-next");
    nextBtn.style = `cursor:pointer`;
    const prevBtn = document.querySelector(".tbSlider-prev");
    prevBtn.style = `opacity: 0`;
    const sliderItemWidth = sliderItems[0].offsetWidth;
    const sliderLength = sliderItems.length;
    let positionX = 0;
    let index = 0;
    console.log(sliderItems.length);

    nextBtn.addEventListener("click", function(){
        handleChangSlide(1);
    });

    prevBtn.addEventListener("click", function(){
        handleChangSlide(-1);
    });

    function handleChangSlide(direction) {
        if (direction == 1) {
            if (index >= sliderLength - 5) {
                index = sliderLength - 5;
                positionX = - sliderItemWidth*(sliderLength - 5);
                return;
            } else index++;
            positionX = positionX - sliderItemWidth;
            sliderMain.style = `transform: translateX(${positionX}px)`;
            // console.log(index);
            // console.log(sliderItemWidth);
            // console.log(positionX);
        }
        else if (direction == -1) {
            if (index <= 0) {
                index = 0;
                positionX = 0;
                return;
            } else index--;
            positionX = positionX + sliderItemWidth;
            sliderMain.style = `transform: translateX(${positionX}px)`;
            // console.log(index);
            // console.log(sliderItemWidth);
            // console.log(positionX);
        }
        if (index <= 0) {
            nextBtn.style = `opacity: 1`;
            prevBtn.style = `opacity: 0`;
            nextBtn.style = `cursor:pointer`;
        }
        else if (index >= sliderLength - 5) {
            nextBtn.style = `opacity: 0`;
            prevBtn.style = `opacity: 1`;
            prevBtn.style = `cursor:pointer`;
        } else {
            nextBtn.style = `opacity: 1`;
            prevBtn.style = `opacity: 1`;
            prevBtn.style = `cursor:pointer`;
            nextBtn.style = `cursor:pointer`;
        }
    }
});

//Script to New Arrivals Slider
window.addEventListener("load", function(){
    const slider = document.querySelector(".naBookList");
    const sliderMain = document.querySelector(".naSlick-track");
    const sliderItems = document.querySelectorAll(".naSlick-slide");
    const nextBtn = document.querySelector(".naSlider-next");
    nextBtn.style = `cursor:pointer`;
    const prevBtn = document.querySelector(".naSlider-prev");
    prevBtn.style = `opacity: 0`;
    const sliderItemWidth = sliderItems[0].offsetWidth;
    const sliderLength = sliderItems.length;
    let positionX = 0;
    let index = 0;
    console.log(sliderItems.length);

    nextBtn.addEventListener("click", function(){
        handleChangSlide(1);
    });

    prevBtn.addEventListener("click", function(){
        handleChangSlide(-1);
    });

    function handleChangSlide(direction) {
        if (direction == 1) {
            if (index >= sliderLength - 5) {
                index = sliderLength - 5;
                positionX = - sliderItemWidth*(sliderLength - 5);
                return;
            } else index++;
            positionX = positionX - sliderItemWidth;
            sliderMain.style = `transform: translateX(${positionX}px)`;
            // console.log(index);
            // console.log(sliderItemWidth);
            // console.log(positionX);
        }
        else if (direction == -1) {
            if (index <= 0) {
                index = 0;
                positionX = 0;
                return;
            } else index--;
            positionX = positionX + sliderItemWidth;
            sliderMain.style = `transform: translateX(${positionX}px)`;
        }
        if (index <= 0) {
            nextBtn.style = `opacity: 1`;
            prevBtn.style = `opacity: 0`;
            nextBtn.style = `cursor:pointer`;
        }
        else if (index >= sliderLength - 5) {
            nextBtn.style = `opacity: 0`;
            prevBtn.style = `opacity: 1`;
            prevBtn.style = `cursor:pointer`;
        } else {
            nextBtn.style = `opacity: 1`;
            prevBtn.style = `opacity: 1`;
            prevBtn.style = `cursor:pointer`;
            nextBtn.style = `cursor:pointer`;
        }
    }
});
