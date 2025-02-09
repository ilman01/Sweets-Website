const contentgrid = `
<section class="container my-5">
    <div class="row g-4">
        <div class="col-lg-4 cell">
    <div onclick="location.href='/video/If-You-Have-a-Dream-Reprise/';" class="card clickable">
        <img src="/thumbnails/If-You-Have-a-Dream-Reprise.webp" class="card-img-top" style="height: 360; width: 640;" alt="Thumbnail">
        <div class="card-body">
            <h6 class="search-show text-muted fw-light">Fancy Nancy</h6>
            <h5 class="card-title"><a class="search-title text-decoration-none text-black">If You Have a Dream (Reprise)</a></h5>
            <p class="card-text">You'll always find a way!</p>
        </div>
    </div>
</div>
<div class="col-lg-4 cell">
    <div onclick="location.href='/video/My-2024-Medley/';" class="card clickable">
        <img src="/thumbnails/My-2024-Medley.webp" class="card-img-top" style="height: 360; width: 640;" alt="Thumbnail">
        <div class="card-body">
            <h6 class="search-show text-muted fw-light">Original Remix</h6>
            <h5 class="card-title"><a class="search-title text-decoration-none text-black">My 2024 Medley</a></h5>
            <p class="card-text">Here's a compilation of my favorite moments in 2024.</p>
        </div>
    </div>
</div>
<div class="col-lg-4 cell">
    <div onclick="location.href='/video/Grow-With-Me/';" class="card clickable">
        <img src="/thumbnails/Grow-With-Me.webp" class="card-img-top" style="height: 360; width: 640;" alt="Thumbnail">
        <div class="card-body">
            <h6 class="search-show text-muted fw-light">Alice's Wonderland Bakery</h6>
            <h5 class="card-title"><a class="search-title text-decoration-none text-black">Grow With Me</a></h5>
            <p class="card-text">Let's unlock the corners of our world!</p>
        </div>
    </div>
</div>
<div class="col-lg-4 cell">
    <div onclick="location.href='/video/My-2023-Medley/';" class="card clickable">
        <img src="/thumbnails/My-2023-Medley.webp" class="card-img-top" style="height: 360; width: 640;" alt="Thumbnail">
        <div class="card-body">
            <h6 class="search-show text-muted fw-light">Original Remix</h6>
            <h5 class="card-title"><a class="search-title text-decoration-none text-black">My 2023 Medley</a></h5>
            <p class="card-text">Here's a compilation of my favorite moments in 2023.</p>
        </div>
    </div>
</div>

    </div>
</section>
`
document.getElementById("grid-below").insertAdjacentHTML("afterend", contentgrid);