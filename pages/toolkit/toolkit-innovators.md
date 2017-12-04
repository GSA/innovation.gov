---
layout: toolkit-subpage
title: Engage Innovators and Outside Government
description: Lorem ipsum dolor sit amet,
vertical: innovators
permalink: /toolkit/innovators/
summary: 'Learn more about Innovation.gov and the Better Government Movement'
banner-heading: The Better Government Toolkit Lorem ipsum dolor sit amet, consectetur adipiscing. 
class: innovators-background
---

{% include toolkit-banner.html %}


{% include toolkit-verticals.html %}

<div class="innovators-background toolkit-button-group-small">
	<div class="usa-grid">
	<a class="usa-button" href="#citizen-science">Crowdsourcing and Citizen Science</a>
	<a class="usa-button" href="#engaging-startups">Engaging Startups</a>
	<a class="usa-button" href="#prizes-challenges">Prizes and Challenges</a>
	<a class="usa-button" href="#public-engagement">Public Engagement</a>
	</div>
</div>


{% for section in site.toolkit %}
{% if section.vertical == page.vertical %}
{{ section.output }}
{% endif %}
{% endfor %}

{% include box-get-connected.html %}