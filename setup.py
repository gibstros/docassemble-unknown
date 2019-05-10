import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.py', '*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.unknown',
      version='',
      description=(''),
      long_description='# Docassemble Legal Motion Tutorial\r\nA simple example of a Docassemble interview that automates a Word document to create a motion to dismiss and introduces you to basic Docassemble concepts. You do not need to be a programmer or a lawyer to complete this tutorial.\r\n\r\nCreated by [Quinten Steenhuis](https://github.com/nonprofittechy) and [Rina Padua](https://github.com/Rinapadua) at [Greater Boston Legal Services](https://www.gbls.org).\r\n\r\nThis tutorial was created to make use of features in Docassemble Version 0.2.39 (released in March, 2018) and should work with any later version.\r\n\r\n## How to use this tutorial\r\nYou can use this demo repository to learn the basics of creating a guided interview in Docassemble with a best-practices workflow for an individual or a small team. There are many ways to use Docassemble. When you complete this tutorial you will understand how to:\r\n\r\n* Use a Microsoft Word document as a template for your guided interview\r\n* Understand the most common datatypes in Docassemble\r\n* Use basic logic and conditional statements in a template and in the guided interview\r\n* Use Google Drive sync integration to make editing templates a simple part of the interview workflow\r\n* Use GitHub integration for version control in Docassemble\r\n\r\nYou can use Docassemble without setting up GitHub or Google Drive. Google Drive makes the process of editing Microsoft Word templates much easier and more natural. GitHub integration [will help you](https://www.git-tower.com/learn/git/ebook/en/desktop-gui/basics/why-use-version-control) better work in a team, recover from mistakes in your code, and offer a helpful backup of your work at different points in time.\r\n\r\n## Basic concepts of document assembly\r\n![Overview of Document Assembly](https://gblsma.github.io/docassemble-MotionTutorial/images/Untitled%20Diagram.png)\r\n\r\nThe document assembly process can be separated into 3 logical steps: gathering information from the user in an interview, applying logical reasoning to the information, and finally assembling the information into a formatted document. A common scenario is completing a letter or legal pleading, where one or more blanks (called `variables` or `fields`) will be completed using responses obtained in the interview process. It is a greatly advanced version of search and replace.\r\n\r\nDocassemble adds some special features that make it especially compelling for use in document assembly.\r\n* You can pull in information from other sources on the Internet, such as Google Maps, and apply logical reasoning to it.\r\n* You have access to a full featured object oriented programming language, Python, and all the thousands of modules that have been built by others\r\n* Advanced features like interviews over text messaging, electronic signatures, and even artificial intelligence in the form of machine learning are all built-in.\r\n\r\nDocassemble has a learning curve, but as your confidence and skills grow, you won\'t find yourself limited by the platform as it is as flexible as the Python programming language itself. Yet even non-programmers will find that they can get started with Docassemble pretty quickly.\r\n\r\n## A note about the technologies used in Docassemble\r\nDocassemble makes use of many different component parts. Usually the Docassemble [documentation](https://docassemble.org/docs.html) contains everything you need to know about those components. Sometimes you run into a gap in the documentation and may decide to do your own research. Here are some of the technologies that we use in our demonstration:\r\n\r\n* YAML for the interview file format.\r\n* Python for logic in the interview and template.\r\n* Mako for formatting questions in the interview file.\r\n* Jinja2 for formatting answers in your template.\r\n\r\nThis tutorial includes everything you need to know about those technologies to complete the tutorial. However, it can helpful to know what terms to Google if you run into a stumbling block. The [Docassemble Slack channel](https://join.slack.com/t/docassemble/shared_invite/enQtMjQ0Njc1NDk0NjU2LTAzYzY5NWExMzUxNTNhNjUyZjRkMDg0NGE2Yjc2YjI0OGNlMTcwNjhjYzRhMjljZWU0MTI2N2U0MTFlM2ZjNzg) is also an excellent place to get troubleshooting assistance when a question is not answered in the [documentation](https://docassemble.org/docs.html).\r\n\r\n## Getting started\r\nFollow the comprehensive Docassemble documentation for these first few steps:\r\n\r\n1. [Install Docassemble](https://docassemble.org/docs/docker.html#install). If you just want to try out Docassemble, we recommend installing Docassemble on your laptop or workstation with [Docker](https://www.docker.com/). You may need to [enable virtualization extensions](https://www.intel.com/content/www/us/en/support/articles/000007139/server-products.html) in your computer\'s BIOS settings to run Docker.\r\n1. Create a new account on [GitHub](https://www.github.com) and [Google](https://accounts.google.com/SignUp) if you don\'t already have accounts on both platforms.\r\n1. Enable [GitHub](https://docassemble.org/docs/installation.html#github) and \r\n  [Google Drive Sync](https://docassemble.org/docs/installation.html#google%20drive) integration.\r\n1. Create a folder in Google Drive called `docassemble-playground` (or another name of your choice).\r\n1. Add your GitHub and Google accounts from the Profile menu in Docassemble. Connect Google Drive to the folder you created above, `docassemble-playground`.\r\n1. [Fork](https://github.com/GBLSMA/docassemble-tutorial-motion#fork-destination-box) [this repository](https://github.com/GBLSMA/docassemble-MotionTutorial/#fork-destination-box) on GitHub.\r\n1. [Pull](https://docassemble.org/docs/playground.html#packages) the forked repository into your playground from Folders `|` Packages menu. Make sure you pull the repository that you created by *forking* this repository. Forking will make a copy of the repository that you can update and change as much as you like.\r\n\r\n![Playground Overview](https://gblsma.github.io/docassemble-MotionTutorial/images/Package-overview.png)\r\n\r\n![Pull a package](https://gblsma.github.io/docassemble-MotionTutorial/images/Pull-package.png)\r\n\r\n\r\n### Configure Microsoft Word to work with Docassemble\r\nTo prevent problems, it\'s recommended that you [turn off automatic smart quotes](https://support.office.com/en-us/article/change-curly-quotes-to-straight-quotes-and-vice-versa-017963a0-bc5f-486b-9c9d-0ec511a8fb8f) while creating templates in Microsoft Word for Docassemble. Instructions vary. In recent versions of Word, you can turn off smart quotes by clicking File | Options | Proofing, selecting Autocorrect and uncheck the box "Smart quotes with straight quotes" under "Replace as you type" on both the Autoformat and Autoformat as you type tabs.\r\n\r\n### A tour of the Playground\r\n![Playground Overview](https://gblsma.github.io/docassemble-MotionTutorial/images/Playground-Overview.png)\r\n\r\nThis is a view of the Docassemble playground. You start out in the interview editing mode.\r\n\r\n1. The Folders button lets you access different sections of the playground. You\'ll use this menu to switch between saving your changes to GitHub, uploading new files, and editing templates.\r\n1. The main window that fills your screen is a text area where you can edit the interview script.\r\n1. The list of variables can be used as a reference while you\'re working on the interview.\r\n\r\n### How the Playground, Github, Google Drive, and the Interview and Template all connect\r\n![Docassemble Overview](https://gblsma.github.io/docassemble-MotionTutorial/images/docassemble-workflow.png)\r\n\r\nThe diagram above shows how Google Drive, Github, the interview, and the template are all connected.\r\n1. The template is the final document you want to print or file in court. Edit the templates in Microsoft Word. Formatting goes here.\r\n1. Save your templates on Google Drive, and sync them to the Playground.\r\n1. Your interview is used to "fill in the blanks" in the template. Edit interviews in the Playground.\r\n1. As you complete each task to develop your interview, `commit` your work in progress to Github. You can also sync to Google Drive to make a local copy of your interview and template files.\r\n1. Variables are placeholders that can be filled-in with questions during the interview and then referenced in the document template.\r\n\r\n### Files included in the demo project \r\nThis sample project includes several files to get you started:\r\n\r\n#### Interview Files\r\n* interview-skeleton.yml (A basic outline of an interview that assembles a Word Document. Start with this)\r\n* interview-basic.yml (A completed version of the basic interview. Use for reference only)\r\n* interview-withlogic.yml.yml (A completed version of the interview that uses logic. Use for reference only)\r\n\r\n#### Template Files\r\n* Motion to Dismiss-Original.docx (The original file that we will edit to automate it)\r\n* Motion to Dismiss-Final.docx (A completed version of the template. Use for reference only)\r\n\r\n## Testing the demo interview\r\nIn the Playground, select the `interview-skeleton.yml` file.\r\n\r\nClick the "Save and Run" button to see how the interview works.\r\n![Playground Save and Run button](https://gblsma.github.io/docassemble-MotionTutorial/images/playground-run.png)\r\n\r\nYou\'ll see a screen that lets you download the Word document. Notice how no questions are asked yet. That\'s because\r\nwe haven\'t added any and there are no *variables* in the template yet that need to be defined. This interview simply outputs a Word document with no customizations.\r\n\r\nOnce we add variables to the template, Docassemble will work backwards to try to ask whatever questions are needed to define those variables.\r\n\r\n## Making your first change to a template\r\nLet\'s start by opening our Word document, `Motion to Dismiss-Original.docx` in the `docassemble-playground` folder in your Google Drive account. You should *sync* this folder to your local computer for the simplest workflow.\r\n\r\nTry making a change anywhere in the document. A classic first programming exercise is to output the text "Hello, World."\r\nTry adding the text "Hello, World" somewhere in the document and save the file.\r\n\r\nWait 10-20 seconds, and click the Sync button in the playground again. Try running the interview one more time and verify that the text "Hello, World" is now in your template file.\r\n\r\n## Making your first edit to an interview\r\nInterviews use `YAML` syntax. If you run into a problem with your interview file, it may help to know that you can Google YAML concepts.\r\n\r\nIn the Playground, select the `interview-skeleton.yml` file. You should notice that the interview file contains two different sections: a "[metadata](https://docassemble.org/docs/initial.html#metadata)" section, and an [attachment](https://docassemble.org/docs/documents.html#attachment) block that begins with the line "Mandatory" that includes the filename `Motion to Dismiss-Original.docx`. It may be useful to know that each section, separated by three dashes `---`, is called a document in the `YAML` file format of a docassemble interview. Each interview page will have its section in the interview file. Indentation is important in the interview file. It tells Docassemble how to interpret the information in the interview file. Docassemble makes it easy to set the right indentation by using the `[TAB]` key.\r\n\r\nWe\'ll start by customizing the page where we can download our document. Let\'s try adding a [subquestion](https://docassemble.org/docs/questions.html#subquestion) instruction to our download screen. Review the [documentation for a subquestion instruction](https://docassemble.org/docs/questions.html#subquestion).\r\n\r\nLet\'s change our download page to include the text "Hello, Download.". Try it on your own first, then read ahead. \r\n\r\nTo do this, your interview file should now have a line directly underneath the line that begins with `Your documents are ready.` that looks like this:\r\n```yaml\r\nsubquestion: |\r\n  Hello, Download.\r\n```\r\n\r\nNotice the vertical pipe `|`. It\'s a best practice to include this when you type in text to avoid glitches with Docassemble. Whenever you use it, make sure to include a space after the `:` and indent the following line. Two spaces is the traditional indent in Docassemble, and hitting the [TAB] key is a quick way to enter those two spaces.\r\n\r\nRun the interview again and confirm that the download screen now includes the text `Hello, Download.`\r\n\r\nNext try updating the metadata section so that you are the author of the interview. Try updating the title and short title to see how they change the interview when viewed with different browser window sizes.\r\n\r\n## Understanding code blocks\r\n[Code](https://docassemble.org/docs/code.html) blocks allow us to add logic to an interview. You don\'t need to be a programmer to use `Code` blocks. `Code` blocks use `Python` syntax. If you get stuck or run into an error, Googling `Python` concepts will help you solve your problem.\r\n\r\nLet\'s create a very basic code block using the [example](https://docassemble.org/docs/code.html#simpleexamples) from the Docassemble documentation. This will also be our first introduction to variables. `Variable` will be used as a synonym for `field` in this tutorial.\r\n\r\nAdd a new section into your `interview-skeleton.yml` file. Don\'t forget to begin it with `---` on its own line. Let\'s assign the value 2 + 2 to a new variable named `answer`. Your completed code block should look like this:\r\n\r\n```yaml\r\n---\r\ncode: |\r\n  answer = 2 + 2\r\n```\r\n\r\nNow lets edit our `attachment` block subquestion to state "The answer is (the value of the answer variable)". Refer back to the [example](https://docassemble.org/docs/code.html#simpleexamples) to understand how to display a variable in a question. This is our first introduction to displaying a variable in an interview. The main thing to know is that variables can be used in a question by surrounding them by `${variable_name}`. Try it on your own first. When you are finished, your attachment block should look like this:\r\n\r\n```yaml\r\nquestion: |\r\n  Your documents are ready. Please print and file!\r\nsubquestion: |\r\n  Hello, Download. The answer is ${answer}.\r\n```\r\n\r\nFinally, lets edit our locally saved template `Motion to Dismiss-Original.docx` to include the `answer` variable as well. Try it on your own first by referring to the [Filling DOCX Templates](https://docassemble.org/docs/documents.html#docx template file) documentation. When you are finished, your template should include text that looks like this:\r\n\r\n```\r\nHello, World. The Answer is {% raw %}{{ answer }}{% endraw %}\r\n```\r\n\r\nNotice that while in an interview question, we display a variable like this: `${variable_name}` but in our template, we include a variable by surrounding it with double brackets like this: {% raw %}{{variable_name}}{% endraw %}.\r\n\r\nClick the `GD` button to sync the playground with Google Drive and update the copy of the Word file in our Docassemble playground.\r\n\r\nRun the interview one more time to verify your changes were made.\r\n\r\n## Committing your first changes to Github\r\nLet\'s save our work so far. It\'s a good practice to commit to Github whenever you make a working change to your interview or template.\r\n\r\nUse the Folders menu to navigate to the Packages page. Look over the fields on this page. Notice that if you have multiple packages that you are working on, the package name will be a dropdown menu that you can use to select the package that you wish to update.\r\n![Package Screen](https://gblsma.github.io/docassemble-MotionTutorial/images/Package-firstcommit.png)\r\n\r\nTry updating the Author and Author Email to your own name. Notice that you can select files from the Playground to include the package. If you want to add additional files to the package later, here is where you will do it. Only files that you select on this screen will be committed to Github.\r\n\r\nScroll down to the bottom of the page and click Save, and then the Github button.\r\n\r\n![Github button](https://gblsma.github.io/docassemble-MotionTutorial/images/github-button.png)\r\n\r\nSet the Commit message to something descriptive, such as "Added \'Hello, World\'"\r\n![Github commit](https://gblsma.github.io/docassemble-MotionTutorial/images/Github-commit.png)\r\n\r\n## Building the demo interview\r\nSo far we\'ve told you exactly what to include in the interview and template. For this stage of the tutorial, you will need to do some thinking on your own. Building a guided interview has 3 basic steps:\r\n\r\n1. Deciding what information we need to gather and coming up with descriptive `variable` names for each item of information.\r\n1. Creating interview screens to gather the information.\r\n1. Include the answers you gathered in the interview with formatting in your template.\r\n\r\n### Fields: Identifying the information we need to gather\r\nLook at the sample template `Motion to Dismiss-Original.docx`. Think about the information we need to gather in the following categories:\r\n1. Parties\r\n1. Locations\r\n1. Dates\r\n1. Conclusions and facts needed to reach those conclusions.\r\n\r\nTry it on your own first. Mark any information in the template that will need to change (you can print and highlight on a piece of paper or write it in a separate document such as a spreadsheet).\r\nWe will need to know:\r\n* The county\r\n* The name of the court\r\n* The Landlord\'s name\r\n* The Tenant\'s name\r\n* The Tenant\'s address and phone number\r\n* Every reason for dismissing the case, numbered 1-3 in the example document.\r\n* The date of service\r\n* The type of service\r\n\r\nWrite down logical variable names for each piece of information. Docassemble variables should be:\r\n1. Short\r\n1. Readable (ie., usually you should spell out a word without abbreviations).\r\n1. Lowercase\r\n1. Include `_` to separate words.\r\n1. Cannot begin with a number but may include a number.\r\n\r\nDocassemble `fields` come in different types, and there are special capabilities that come with each type. Some of the key types you will use in this interview include:\r\n* [Dates](https://docassemble.org/docs/fields.html#date)\r\n* [Yesno](https://docassemble.org/docs/fields.html#fields%20yesno) (True/False, or Boolean values) are easy to use in logical statements.\r\n* [Numbers](https://docassemble.org/docs/fields.html#numbers)\r\n* [Text](https://docassemble.org/docs/fields.html#plaintext)\r\n* [Multiple Choice](https://docassemble.org/docs/fields.html#select) `fields` are best used when there is a limited set of valid options.\r\n\r\nFor each `variable` in your list, think about what type of `field` will best represent it.\r\n\r\nIf you get stuck, look at the `interview-basic.yml` file for one approach to solving the problem.\r\n\r\n### Writing interview questions\r\nWe will now need to create an interview screen to gather all of the information. We could create a single page that includes all of the variables. This might be very messy and hard to read. A better practice is to group the related questions together. Try it on your own first. Sketch out 5-6 screens to start.\r\n\r\nA logical grouping might be:\r\n1. The tenant\'s name, address, and phone number\r\n2. The court name and county\r\n3. The landlord\'s name\r\n4. The bases for dismissal\r\n5. The service date and type.\r\n\r\nOnce you have come up with a list of both `variable` names and a logical grouping for your questions, start adding the question blocks into your `interview-skeleton.yml` file. The Docassemble documentation groups `questions` in various places. For most screens in your interview, you will almost always want to use a fields statement that looks like the one below. Learn more about the `fields` statement [here](https://docassemble.org/docs/fields.html#fields).\r\n\r\n```yaml\r\n---\r\nquestion: |\r\n  Fields Demo\r\nsubquestion: |\r\n  This is a question that demonstrates using a Fields statement\r\nfields:\r\n  - Did it happen? : my_yesno_variable\r\n    datatype: yesno\r\n  - What date did it happen? : my_date_variable\r\n    datatype: date\r\n  - Tell us where it happened: my_text_variable\r\n```\r\n\r\nA few things to pay attention to: \r\n* notice that the `question` `subquestion` and `fields` statement are all aligned with the leftmost column. The contents of each `statement` are indented with a [TAB] or two spaces. The indents must match each other.\r\n* Each `field` begins with an indent and a dash `-`.\r\n* The basic format of each question is a description, followed by a colon, followed by the name of the variable where the information will be stored.\r\n* The `date` and `yesno` variables are followed by an indented line and a `datatype` statement. The `text` variable does not. Text is the default datatype in Docassemble so does not need to be specified, but special datatypes do.\r\n\r\nIf you get stuck, look at the `interview-basic.yml` file for one approach to solving the problem.\r\n\r\nIt\'s a good idea to test the interview as you go along. A quick way to test a question is to temporarily mark it as "`mandatory: True`". That will force Docassemble to ask the question.\r\n\r\n### Putting it all together\r\nOnce you have created the interview questions, it\'s time to start replacing the text in the template with the variable names. **Notice that it is important to update the interview before updating the template. Your interview will generate an error if a variable is used in the template before there is a question that defines it.**\r\n\r\nIn the Word Document template `Motion to Dismiss-Original.docx`, start by replacing one or two of the items with the `variable` name. For example, if you chose to name the `variable` holding the name of the court with the logical `court_name`, replace the text "Culver Court" with {% raw %}{{ court_name }}{% endraw %}.\r\n\r\nBefore going further, save your template, sync it from Google Drive to your playground, and run the interview to see if it works.\r\n\r\nSo far we have explained how to use a `text` `variable` in a template. What about a True/False or `yesno` variable? Use [if statements](https://docassemble.org/docs/documents.html#docx%20template%20file). Below is an example of an `if` statement.\r\n\r\n```jinja\r\n{% raw %}\r\n{%p if my_yesno_variable %}\r\nThis text only shows if my_yesno_variable is True.\r\n{%p endif %}\r\nThis text always displays.\r\n{% endraw %}\r\n```\r\nThere are a few things to notice. First, we are no longer using the double brackets {% raw %}{{ var }}{% endraw %}. Instead, we are using a single bracket followed by a % sign. {% raw %}{% ... %}{% endraw %}. This syntax is used for control structures in Word templates. Also, notice the `p` following the `%`. This tells Docassemble to remove the line that has the `if` statement on it. Use this whenever the line with the `if` statement doesn\'t contain any other information. A {% raw %}{%p if %}{% endraw %} statement must always be matched with a {% raw %}{%p endif %}{% endraw %} statement. If you use the `p` in the opening line, it also needs to be used in the closing line, and vice versa.\r\n\r\nYou can go very far in creating any template that represents a legal pleading just by using `text` variables and `yesno` variables with `if` statements. As an exercise, finish replacing all of the text you want to be able to change in your template with the variable names you gather in the interview. Use the `if` control structure for text that only conditionally displays. Remember to use the {% raw %}{%p if ... %}{% endraw %} style for a numbered list.\r\n\r\nIf you are stuck, take a look at the `Motion to Dismiss-Final.docx` file to see one possible solution.\r\n\r\nIf you are curious, for advanced use other [Jinja2 control structures](http://jinja.pocoo.org/docs/2.10/templates/#list-of-control-structures) can also be used to control the display of text in the template. For example, when displaying a list of information, you may want to make use of a `for` statement.\r\n\r\n### Applying legal reasoning\r\nYou may have wondered how the end user of the interview is supposed to know the bases for dismissal. One approach would be to include detailed instructions in the text of the interview. This would involve giving the tenant a mini-primer in eviction law and asking them to apply their new found knowledge to their own situtation. However, a better approach is to use the conditional statement features of Docassemble to do the legal reasoning for the tenant. One of the most powerful features of a guided interview platform like Docassemble is the possibility to simulate a "lawyer in a box" at the other end of the interview.\r\n\r\nHere are the basic legal rules necessary to understand each basis for dismissal:\r\n\r\n1. A landlord cannot terminate a tenancy with a 14 day notice to quit if the tenant paid all rent owed before the landlord sent the notice.\r\n1. If the tenant has a lease, the tenant can "cure" the notice to quit by paying all of the rent owed on or before the "answer date". If the tenant has a tenancy at will (month to month), the tenant can "cure" the notice to quit by paying all rent owed on or before 10 days of receiving the notice to quit.\r\n1. If the landlord accepted any rent after sending the notice to quit without including a "reservation of rights" in the notice to quit or immediately when accepting the rent, the termination may be "waived". A reservation of rights looks like this: "any payments will be accepted for use and occupancy only and will not reinstate the tenancy."\r\n\r\nA highly readable primer on Massachusetts Eviction law can be found here: http://www.masslegalhelp.org/legal-tactics. Check out [Chapter 12](http://www.masslegalhelp.org/housing/lt1-chapter-12-evictions.pdf), the section titled "Stopping an Eviction Before a Trial" to see more detailed information about the basic rules above.\r\n\r\n#### Break the information required into smaller logical elements\r\nGiven the rules above, what additional information do we need to know to decide if any of the three bases for dismissal apply? Try it on your own first. When you have finished, you should have a list that looks like the list below:\r\n\r\n* What was the answer date?\r\n* Does the tenant have a tenancy by lease or at will?\r\n* When did the tenant receive the notice to quit?\r\n* When did the tenant last pay rent?\r\n* Did the tenant pay the full amount of rent owed?\r\n* Did the notice to quit contain a reservation of rights?\r\n\r\nRemove the interview section that asks directly if the bases for dismissal apply. Instead, we will create new interview screens that ask the facts listed above. Try it on your own first.\r\n\r\nIf you get stuck, look at the file `interview-withlogic.yml` for one approach to solving the problem.\r\n\r\n#### Apply the logical rules to our interview\r\nNotice that we do not need to make any changes to our template to add this additional logic. A `code` block in Docassemble can set a variable based on the value of another variable using a logical `if` statement.\r\n\r\nWe can include all of our logical rules in a single code block. To get you started, below is an example logical block to test one scenario, a tenant who has a lease curing the notice to quit by paying all rent due sometime before the Answer date. The `if` statement in the interview is similar to the one we used in the template already.\r\n\r\n```yaml\r\n---\r\ncode: |\r\n  if tenancy_type == \'lease\':\r\n    if tenant_paid_all_rent_due and tenant_pay_date <= answer_date:\r\n      tenant_cured = True\r\n    else:\r\n      tenant_cured = False\r\n```\r\n\r\nTry completing the exercise for the remaining logical scenarios: a tenant who has a tenancy at will, a tenant who paid before receiving the notice to quit, and a tenant whose landlord waived the notice to quit by accepting rent without a reservation of rights.\r\n\r\nYou may get stuck with the date math as it is a moderately advanced topic. Docassemble has [special functions for working with dates](https://docassemble.org/docs/functions.html#date%20functions). Here\'s an example that sets the my_date variable to a date 10 days after the date we gathered in the interview:\r\n\r\n```yaml\r\n---\r\ncode: |\r\n  my_date = gathered_date + date_interval(days=10)\r\n```\r\nSee the [documentation](https://docassemble.org/docs/functions.html#date_interval) for `date_interval` for more examples. \r\n\r\nIf you are stuck, take a look at the `interview-withlogic.yml` file for one possible solution.\r\n\r\n## Room for improvement\r\nOnce you have completed the basic tutorial and tried adding in logic, here are some improvements you should try making:\r\n\r\n* Read about Docassemble [objects](https://docassemble.org/docs/objects.html), especially the built-in object types Individual and Address, and the special [Legal object](https://docassemble.org/docs/legal.html) types Case and Court. Refactor your variable names to make use of the special features of Objects and the useful dot (.) notation that Objects allow to keep related variables together.\r\n* Read about the Docassemble [include_docx_template](https://docassemble.org/docs/functions.html#include_docx_template) function. Replace the case caption with a separate Word document that you include into the parent template. Replace the name, address and signature line with a separate Word document as well. In future projects, this will help you keep formatting consistent across your documents.\r\n* Create a Google API key and enable the [Address Autocomplete](https://docassemble.org/docs/fields.html#address%20autocomplete) functionality that Docassemble supports on the screen that gathers the tenant\'s address.\r\n* Try [decorating](https://docassemble.org/docs/modifiers.html#decoration) your questions with a Font Awesome or Material Design icon. For example, find the shortcut code that represents a gavel and add it to the top right corner of the screen that asks for the name of the court the motion will be heard in.\r\n* Add a screening question to your interview that tells the tenant that they do not have a lawyer and requires them to acknowledge that to complete the interview. Look at the Docassemble [demonstration](https://docassemble.org/demo.html) interview and read more about [events](https://docassemble.org/docs/questions.html#event) to complete this exercise.\r\n\r\n# Conclusion\r\nWe hope that this tutorial will help you develop your own guided interviews in Docassemble! This tutorial is provided free as a service for anyone who wants to develop on Docassemble. If you notice typos or want to add additional content to this tutorial, pull requests are welcome. [Fork](https://github.com/GBLSMA/docassemble-MotionTutorial/edit/gh-pages/README.md#fork-destination-box) this repository and edit README.md in the gh-pages branch, make any changes, and then submit your pull request.\r\n',
      long_description_content_type='text/markdown',
      author='System Administrator',
      author_email='admin@admin.com',
      license='',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/unknown/', package='docassemble.unknown'),
     )
