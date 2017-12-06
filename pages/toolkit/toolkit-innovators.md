---
layout: toolkit-subpage
title: Engage Innovators and Outside Government
description: Pathways to engage innovators inside and outside of government through public-private partnerships, startup engagement, prizes and challenges, and citizen science and crowdsourcing.
vertical: innovators
permalink: /toolkit/innovators/
summary: 'Learn more about Innovation.gov and the Better Government Movement'
banner-heading: The Better Government Toolkit provides approaches, policies, and resources to build a better government through innovation.
class: innovators-background
---

{% include toolkit-banner.html %}


{% include toolkit-verticals.html %}

<div class="innovators-background toolkit-button-group-small">
	<div class="usa-grid">
	<a class="usa-button" href="#public-engagement">Public Engagement</a>
	<a class="usa-button" href="#engaging-startups">Engaging Startups</a>
	<a class="usa-button" href="#prizes-challenges">Prizes and Challenges</a>
	<a class="usa-button" href="#citizen-science">Crowdsourcing and Citizen Science</a>
	</div>
</div>


{% for section in site.toolkit %}
{% if section.vertical == page.vertical %}
{{ section.output }}
{% endif %}
{% endfor %}

{% include box-get-connected.html %}
