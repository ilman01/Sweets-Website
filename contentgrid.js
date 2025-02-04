const contentgrid = `
<section class="container my-5">
    <div class="row g-4 d-flex align-items-center justify-content-center">
        <div class="col-lg-4 cell">
            <div onclick="location.href='/video/My-2024-Medley.html';" class="card clickable">
                <img src="/thumbnails/medley thumbnail - 2024.png" class="card-img-top" style="height: 360; width: 640;" alt="Thumbnail">
                <div class="card-body">
                    <h5 class="card-title"><a class="search-title text-decoration-none text-black">My 2024 Medley</a></h5>
                    <p class="card-text">Here's a compilation of my favorite moments in 2024.</p>
                </div>
            </div>
        </div>

        <div class="col-lg-4 cell">
            <div onclick="location.href='/video/My-2023-Medley.html';" class="card clickable">
                <img src="/thumbnails/medley thumbnail - 2023.png" class="card-img-top" style="height: 360; width: 640;" alt="Thumbnail">
                <div class="card-body">
                    <h5 class="card-title"><a class="search-title text-decoration-none text-black">My 2023 Medley</a></h5>
                    <p class="card-text">Here's a compilation of my favorite moments in 2023.</p>
                </div>
            </div>
        </div>
    </div>
</section>
`
document.getElementById("grid-below").insertAdjacentHTML("afterend", contentgrid);