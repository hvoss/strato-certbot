
import re

print("A new pattern:")
result = re.findall(
  r'<div\s+class="user_package_name_container\s+cep_context">.+?<a\s+'
  r'class="customer-link"\s+href="[^"]*cID=(?P<cID>\d+)[^"]*">.+?'
  r'<div class="package-information">\s*<span[^>]*>(?P<domains>[^/]+?)</span>',
  open("projectPage.html","r").read(),
  re.DOTALL
  )

print("check domain-a.de is in project 7: %s" % [item[0] == '7' for item in result if 'domain-a.de' in item[1]][0])
print("check domain-b.de is in project 6: %s" % [item[0] == '6' for item in result if 'domain-b.de' in item[1]][0])
print("check domain-c.de is in project 5: %s" % [item[0] == '5' for item in result if 'domain-c.de' in item[1]][0])
print("check domain-d.de is in project 4: %s" % [item[0] == '4' for item in result if 'domain-d.de' in item[1]][0])
print("check domain-e.de is in project 2: %s" % [item[0] == '2' for item in result if 'domain-e.de' in item[1]][0])
print("check domain-f.de is in project 2: %s" % [item[0] == '2' for item in result if 'domain-f.de' in item[1]][0])
print("check domain-g.de is in project 1: %s" % [item[0] == '1' for item in result if 'domain-g.de' in item[1]][0])


domains = [
    ['domain-a.de', '7'],
    ['domain-b.de', '6'],
    ['domain-c.de', '5'],
    ['domain-d.de', '4'],
    ['domain-e.de', '2'],
    ['domain-f.de', '2'],
    ['domain-g.de', '1']
]

print()
print("My bad pattern")
for domain in domains:
    result = re.search(
        r'<a\s+class="customer-link"\s+href="[^"]*cID=(?P<cID>\d+)[^"]*">\s*'
        r'<span\s+class="jss_own_packagename">\s*'
        + domain[0].replace('.', r'\.'),
        open("projectPage.html","r").read(),
        re.DOTALL
        )
    print("check %s is in project %s: %s" % (domain[0], domain[1], result != None and result.group('cID') == domain[1]))

print()
print("Actual pattern:")
for domain in domains:
    result = re.search(
        r'<div\s+class="cep_product">\s*<a\s+class="customer-link"\s+href='
        r'"[^"]*cID=(?P<cID>\d+).*<span[^>]*>[^\/]*'
        + domain[0].replace('.', r'\.'),
        open("projectPage.html","r").read(),
        re.DOTALL
        )
    print("check %s is in project %s: %s" % (domain[0], domain[1], result != None and result.group('cID') == domain[1]))
    