Title: Projects
Category: Pages
Template: project

<!-- 
{% extends "base.html" %}
{% block content %}
<div class="project-button" onclick="toggleExpand(this)">
    <div class="project-title">tetrys</div>
    <div class="project-image">
    <img src="{static}/images/tetrys.png" alt="tetrys" />{: .image-process-project-image}
    </div>
</div>
{% endblock %}
{% block CUSTOM_CSS %}
<style>
    .project-button {
        width: 200px;
        background-color: aquamarine;
        cursor: pointer;
        overflow: hidden;
        position: relative;
        transition: background-color 0.3s;
    }

    .project-button:hover {
        background-color: #7fffd4; /* Brighter shade of aquamarine */
    }

    .project-title {
        padding: 10px;
        color: #000;
        background-color: green;
    }

    .project-image {
        opacity: 0;
        transition: opacity 0.3s, transform 0.3s;
    }

    .project-image img {
        width: 100%;
        transition: transform 0.3s;
    }

    .project-button.expanded .project-image {
        opacity: 1;
    }

    .project-button:hover .project-image img {
        transform: scale(1.1); /* Zoom in effect on hover */
    }
</style>
{% endblock %}
{% block additional_js %}
<script>
    function toggleExpand(element) {
        element.classList.toggle('expanded');
    }
</script>
{% endblock %} -->