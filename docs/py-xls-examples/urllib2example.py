import ClientForm
import urllib2
request = urllib2.Request(
    "http://wwwsearch.sourceforge.net/ClientForm/example.html")
response = urllib2.urlopen(request)
forms = ClientForm.ParseResponse(response, backwards_compat=False)
response.close()
form = forms[0]
print form  
original_text = form["comments"]  
form["comments"] = "Blah."
form["favorite_cheese"] = ["brie"]  
form["cheeses"] = ["parmesan", "leicester", "cheddar"]  
form.set_value(["parmesan", "leicester", "cheddar"], name="cheeses")
#form.add_file(open("data.dat"))
#form.add_file(open("data.txt"), "text/plain", "data.txt")
control = form.find_control("comments")
print control.disabled
print control.readonly
control.disabled = False
form.set_all_readonly(False)
control = form.find_control("cheeses", type="select")
print control.name, control.value, control.type
control.value = ["mascarpone", "curd"]
item = control.get("curd")
print item.name, item.selected, item.id, item.attrs
item.selected = False
control = form.find_control(label="select a cheese")
form.set_value(["gouda"], name="cheeses", kind="list")
form.find_control(name="cheeses", kind="list").value = ["gouda"]
form["cheeses"] = ["gouda"]
form.set_value("rhubarb rhubarb", kind="text", nr=0)
form.set_value(["spam"], kind="singlelist", nr=0)
def control_has_caerphilly(control):
    for item in control.items:
        if item.name == "caerphilly": return True
form.find_control(kind="list", predicate=control_has_caerphilly)
for control in form.controls:
    if control.value == "inquisition": sys.exit()
for item in form.find_control("cheeses").items:
    print item.name
cheeses = form.find_control("cheeses")
curd = cheeses.get("curd")
del cheeses.items[cheeses.items.index(curd)]
ClientForm.Item(cheeses, {"contents": "mascarpone",
                          "value": "mascarpone"})
form.set_value_by_label(["Mozzarella", "Caerphilly"], "cheeses")
print "parmesan" in form["cheeses"]
print "parmesan" in [
    item.name for item in form.find_control("cheeses").items if item.selected]
print "caerphilly" in [item.name for item in form.find_control("cheeses").items]
form.find_control("cheeses").get("gorgonzola").selected = True
form.find_control(type="checkbox", nr=2).get("edam").selected = False
form.find_control(id="chz").get(label="Mozzarella").selected = False
form.find_control("smelly").items[0].selected = True  
form.find_control("smelly").items[0].selected = False  
control = form.find_control("cheeses")
print control.get("emmenthal").disabled
control.get("emmenthal").disabled = True
control.set_all_items_disabled(False)
request2 = form.click()  
try:
    response2 = urllib2.urlopen(request2)
except urllib2.HTTPError, response2:
    pass
print response2.geturl()
print response2.info()  
print response2.read()  
response2.close()
