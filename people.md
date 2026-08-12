---
layout: page
title: People
subtitle: The team building Pragament
permalink: /people/
---

<style>
  .people-hero {
    background: linear-gradient(120deg, #f5f7ff 0%, #eef8f4 60%, #fff4e6 100%);
    border-radius: 18px;
    padding: 2rem;
    margin: 1rem 0 2rem;
  }
  .people-hero a,
  .people-table a {
    font-weight: 600;
  }
  .section {
    margin: 2.5rem 0;
  }
  .table-wrap {
    overflow-x: auto;
    border: 1px solid #ececec;
    border-radius: 12px;
    background: #fff;
  }
  .people-table {
    width: 100%;
    margin: 0;
  }
  .people-table th,
  .people-table td {
    padding: 12px 14px;
    vertical-align: middle;
  }
  .people-table thead th {
    background: #f7f7f7;
  }
  .person-link {
    white-space: nowrap;
  }
</style>

<div class="people-hero">
  <h1>Our People</h1>
  <p>
    Pragament is built by a growing team of educators, technologists, and mentors who believe in joyful STEM learning,
    strong English skills, value education, and leadership development.
  </p>
  <p>
    Follow our company updates on
    <a href="https://www.linkedin.com/company/pragament/">LinkedIn</a>.
  </p>
</div>

<div class="section">
  <h2>Current Team</h2>
  <div class="table-wrap">
    <table class="people-table">
      <thead>
        <tr>
          <th>Sno</th>
          <th>Name</th>
          <th>LinkedIn</th>
          <th>Pull Requests</th>
          <th>Date of Joining</th>
        </tr>
      </thead>
      <tbody>
        {% for member in site.data.people.current %}
          <tr>
            <td>{{ forloop.index }}</td>
            <td><a class="person-link" href="{{ '/people/' | append: member.slug | append: '/' | relative_url }}">{{ member.name }}</a></td>
            <td><a href="{{ member.linkedin }}">Profile</a></td>
            <td>
              {% if member.github %}
                {% assign repo_url = site.github.repository_url | default: "https://github.com/pragament/pragament.github.io" %}
                <a href="{{ repo_url }}/pulls?q=is%3Apr+author%3A{{ member.github }}" target="_blank">PRs</a>
              {% else %}
                -
              {% endif %}
            </td>
            <td>{{ member.date_of_joining }}</td>
          </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
</div>

<div class="section">
  <h2>Past Team Members</h2>
  <div class="table-wrap">
    <table class="people-table">
      <thead>
        <tr>
          <th>Sno</th>
          <th>Name</th>
          <th>LinkedIn</th>
          <th>Pull Requests</th>
          <th>Date of Joining</th>
          <th>End Date</th>
          <th>Duration</th>
        </tr>
      </thead>
      <tbody>
        {% for member in site.data.people.past %}
          <tr>
            <td>{{ forloop.index }}</td>
            <td><a class="person-link" href="{{ '/people/' | append: member.slug | append: '/' | relative_url }}">{{ member.name }}</a></td>
            <td><a href="{{ member.linkedin }}">Profile</a></td>
            <td>
              {% if member.github %}
                {% assign repo_url = site.github.repository_url | default: "https://github.com/pragament/pragament.github.io" %}
                <a href="{{ repo_url }}/pulls?q=is%3Apr+author%3A{{ member.github }}" target="_blank">PRs</a>
              {% else %}
                -
              {% endif %}
            </td>
            <td>{{ member.date_of_joining }}</td>
            <td>{{ member.end_date }}</td>
            <td>{{ member.duration }}</td>
          </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
</div>
