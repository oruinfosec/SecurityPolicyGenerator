# Security policy generator

## Introduction

The security policy generator is a tool to generate templated security policies and procedures, based on a base best practice set of documents. These templates cover topics such as physical security, information security, business continuity and privacy.

The template base used here is based on the awesome [KPN Security Policy](https://github.com/KPN-CISO/kpn-security-policy). 

The idea is that you fill in some details, the script generates some templated markdown files, you can then prune and adapt the documents for your needs. 

This documentation doesn't cover the entire scope of ISO 27001 / NIST 800, but produces a good baseline that can be adapted. 

## Usage


Policy generator consists of three working parts: 

1. Fully editable markdown templates
2. **variable.ini** file which consists of every variable from markdown templates
3. **generatePolicy.py** script which fills the templates with **variable.ini** data

Users should fill **variable.ini** file with wanted data and simply run the **generatePolicy.py** script.

Policy Generator works with Python versions **>= 3.3** and **jinja2** library. 

You can install the most recent Jinja2 version using pip:

```
pip install Jinja2
```

Sample run:

[![](http://img.youtube.com/vi/X6P_NVn3N8Q/0.jpg)](http://www.youtube.com/watch?v=X6P_NVn3N8Q "Usage example")

## Best practice

This template consists of parts that are company/organization specific. Certain variables rely heavily on specific documents and organizations should prepare them up front. 

## List of intertwined variables and documents:

**bcm_threats_list**: List of Business Continuity Management threats which should be taken into consideration while doing risk assessment

**password_security_rule**: Guideline for determining assurance levels.

**identity_and_access_management_standard**: Guideline about assurance levels itself.

**physical_access_control_specification**: Specification about Physical Access Control. It should contain highly specific company information.

**physical_security_of_technical_buildings_specification**: Specification about physical security of technical buildings. It should contain highly company specific information about physical security of technical buildings.

**company_preferred_list_of_cryptographic_algorithms**: A document which contains a list of accepted cryptographic algorithms and information about their usage.

**company_logging_guidelines**: Company's guideline about logging process.

**document_scoping_bcm**: Guideline document for scoping business continuity management matters.

**bcm_ia_guideline**: Guideline document which contains details about business continuity management impact analysis.

**requirement_selection_document**: Guideline document which contains a list of certain supplier requirements.

## List of documents without given variables:

**Top level policy document**: Document which provides a set of measures and requirements that the organization must fulfil in their daily practice, including practical means to match such requirements onto the specific situation and needs of individual organizational units and employees.

**Security and continuity management document**: Describing the process of management of security and continuity within the company.

# Warranty

THE SOFTWARE AND CONTENT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Credits

Special thanks to [KPN-CISO](https://github.com/KPN-CISO) for the template files (https://github.com/KPN-CISO/kpn-security-policy).

# Authors

This project was created by Patrik Dolovski ( [Linkedin](https://www.linkedin.com/in/patrik-dolovski-14964513a/) [Github](https://github.com/patdolovs) ) and Bogdan Erdelji ( [Github](https://github.com/bodavk) ), during their tenure as Interns @ Oru.
