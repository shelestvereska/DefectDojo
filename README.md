# DefectDojo

[![OWASP Flagship](https://img.shields.io/badge/owasp-flagship%20project-orange.svg)](https://www.owasp.org/index.php/OWASP_DefectDojo_Project) [![GitHub release](https://img.shields.io/github/release/DefectDojo/django-DefectDojo.svg)](https://github.com/DefectDojo/django-DefectDojo) [![YouTube Subscribe](https://img.shields.io/badge/youtube-subscribe-%23c4302b.svg)](https://www.youtube.com/channel/UCWw9qzqptiIvTqSqhOFuCuQ) ![Twitter Follow](https://img.shields.io/twitter/follow/defectdojo.svg?style=social&label=Follow)

[![Build Status](https://github.com/DefectDojo/django-DefectDojo/actions)](https://github.com/DefectDojo/django-DefectDojo/actions) [![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/2098/badge)](https://bestpractices.coreinfrastructure.org/projects/2098)

![Screenshot of DefectDojo](https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/static/images/screenshot1.png)

[DefectDojo](https://www.defectdojo.org/) is a security orchestration and
vulnerability management platform.
DefectDojo allows you to manage your application security program, maintain
product and application information, triage vulnerabilities and
push findings to systems like JIRA and Slack. DefectDojo enriches and
refines vulnerability data using a number of heuristic algrothims that
improve with the more you use the platform.

## Demo

Try out the demo sever at [demo.defectdojo.org](https://demo.defectdojo.org)

Log in with `admin / defectdojo@demo#appsec`. Please note that the demo is pubicly accessable and regularly reset. Do not put sensitive data in the demo.

## Quick Start

```sh
git clone https://github.com/DefectDojo/django-DefectDojo
cd django-DefectDojo
# building
docker-compose build
# running
docker-compose up
# obtain admin credentials. the initializer can take up to 3 minutes to run
# use docker-compose logs -f initializer to track progress
docker-compose logs initializer | grep "Admin password:"
```

Navigate to <http://localhost:8080>.


## [Documentation](https://defectdojo.github.io/django-DefectDojo/)

### [Getting Started](readme-docs/GETTING-STARTED.md)

### [REST APIs](readme-docs/REST-APIs.md)

### [Client APIs and Wrappers](readme-docs/CLIENT-APIs-AND-WRAPPERS)

### [Release and Branch Model](readme-docs/RELEASE-AND-BRANCH-MODEL.md)

### [Contributing](readme-docs.md)

### [Roadmap](readme-docs/ROADMAP.md)

### [Wishlist](readme-docs/WISHLIST.md)

## Supported Installation Options

* [Docker / Docker Compose](readme-docs/DOCKER.md)
* [godojo](https://github.com/DefectDojo/godojo)


## Community and Getting Involved
Please come to our Slack channel first, where we can try to help you or point you in the right direction:

![Slack](https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/static/images/slack_rgb.png)

Realtime discussion is done in the OWASP Slack Channel, #defectdojo.
[Get Access.](https://owasp-slack.herokuapp.com/)

## Social Media
 [![Twitter](https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/static/images/Twitter_Logo.png)](https://twitter.com/defectdojo)
 [![LinkedIn](https://raw.githubusercontent.com/devGregA/django-DefectDojo/dev/docs/static/images/Linkedin-logo-icon-png.png)](https://www.linkedin.com/company/defectdojo)

Follow DefectDojo on [Twitter](https://twitter.com/defectdojo) and [Linkedin](https://www.linkedin.com/company/defectdojo) for project updates!

## About Us

DefectDojo is maintained by:

* [Greg Anderson](https://www.linkedin.com/in/g-anderson/)
* [Aaron Weaver](https://www.linkedin.com/in/aweaver/) ([@weavera](https://twitter.com/weavera))
* [Matt Tesauro](https://www.linkedin.com/in/matttesauro/) ([@matt_tesauro](https://twitter.com/matt_tesauro))


## Project Moderators

Project Moderators can help you with pull requests or feedback on dev ideas.

* [Alex Dracea](https://www.linkedin.com/in/alexandru-marin-dracea-910b51122/)
* Valentijn Scholten (@valentijnscholten) ([github](https://github.com/valentijnscholten) | [sponsor](https://github.com/sponsors/valentijnscholten) | [linkedin](https://www.linkedin.com/in/valentijn-scholten/))
* Jannik Jürgens
* [Fred Blaise](https://www.linkedin.com/in/fredblaise/)
* [Cody Maffucci](https://www.linkedin.com/in/cody-maffucci)
* Pascal Trovatelli / [Sopra Steria](https://www.soprasteria.com/)
* [Damien Carol](https://www.linkedin.com/in/damien-carol/)
* [Stefan Fleckenstein](https://www.linkedin.com/in/stefan-fleckenstein-6a456a30/)


## Hall of Fame

* Charles Neill ([@ccneill](https://twitter.com/ccneill)) – Charles served as a
    DefectDojo Maintainer for years and wrote some of Dojo's core functionality.
* Jay Paz ([@jjpaz](https://twitter.com/jjpaz)) – Jay was a DefectDojo
  maintainer for years. He performed Dojo's first UI overhaul, optimized code structure/features, and added numerous enhancements.





## Sponsors
[<img src="https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/static/images/10Security-logo.png" github-user="devgrega" alt="10Security" width="250"/>](https://10security.com)
[<img src="https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/static/images/isaac.png" github-user="valentijnscholten" alt="ISAAC" width="250"/>](https://isaac.nl)
[<img src="https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/static/images/timo-pagel-logo.png" github-user="wurstbot" alt="Tim Pagel" width="250" />](https://pagel.pro/)
[<img src="https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/static/images/arrival.png" github-user="ansidorov" alt="ARRIVAL" width=300 />](https://arrival.com)
[<img src="https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/static/images/cloudbees-logo.png" github-user="madchap" alt="Cloudbees" width=300 />](https://cloudbees.com/)
[<img src="https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/static/images/WHP.png" github-user="mtesauro" alt="WeHackPurle" width=300 />](https://wehackpurple.com/)
[<img src="https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/dev/docs/static/images/maibornwolff-logo.png)" github-user="StefanFl" alt="MiabornWolff" width=300 />]((https://www.maibornwolff.de/en))



Interested in becoming a sponsor and having your logo displayed? Please review
our [sponsorship information](readme-docs/SPONSORING.md)

## License

DefectDojo is licensed under the [BSD Simplified license](LICENSE.md)
