
# Cookbooks Gallery


Pythia Cookbooks provide example workflows on more advanced and domain-specific problems developed by the Pythia community. Cookbooks build on top of skills you learn in Pythia Foundations.

<div class="d-sm-flex mt-3 mb-4">
<div class="d-flex gallery-menu">
</div>
<div class="ml-auto d-flex">
<div><button class="btn btn-link btn-sm mx-1" onclick="clearCbs()">Clear all filters</button></div>

<div class="dropdown">

<button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="domainsDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
Domains
</button>
<ul class="dropdown-menu" aria-labelledby="domainsDropdown">
<li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=radar onchange="change();">&nbsp;Radar</label></li>
</ul>
</div>


<div class="dropdown">

<button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="packagesDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
Packages
</button>
<ul class="dropdown-menu" aria-labelledby="packagesDropdown">
<li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=Py-ART onchange="change();">&nbsp;Py-art</label></li>
</ul>
</div>

</div>
</div>
<script>$(document).on("click",function(){$(".collapse").collapse("hide");}); </script>


````{panels}
:column: col-12
:card: +mb-4 w-100
:header: d-none
:body: p-3 m-0
:footer: p-1

---
:column: + tagged-card Py-ART radar

<div class="d-flex gallery-card">
<img src="_static/images/thumbnails/arm_logo.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://cookbooks.projectpythia.org/radar-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Radar Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Max Grover<br/></p>
<p class="my-2">This Project Pythia Cookbook covers the basics of working with weather radar data in Python.
</p>
</div>
</div>


+++
<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Py-ART</span>
<span class="badge bg-primary mybadges">radar</span>
<div
    <a class="reference external" href="https://github.com/ProjectPythiaCookbooks/radar-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythiaCookbooks/radar-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
    <a class="reference external" href="https://binder-staging.2i2c.cloud/v2/gh/ProjectPythiaTutorials/radar-cookbook.git/main"><img alt="Binder" src="https://binder-staging.2i2c.cloud/badge_logo.svg" /></a>
    </div>
</div>


````

<div class="modal-backdrop"></div>
<script src="/_static/custom.js"></script>
