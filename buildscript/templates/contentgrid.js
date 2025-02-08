const contentgrid = `
<section class="container my-5">
    <div class="row g-4">
        {cards}
    </div>
</section>
`
document.getElementById("grid-below").insertAdjacentHTML("afterend", contentgrid);