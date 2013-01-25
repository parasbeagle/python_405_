import uno

localContext = uno.getComponentContext()
resolver = localContext.ServiceManager.createInstanceWithContext( "com.sun.star.bridge.UnoUrlResolver", localContext )
ctx = resolver.resolve( "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
smgr = ctx.ServiceManager
desktop = smgr.createInstanceWithContext( "com.sun.star.frame.Desktop",ctx)
model = desktop.getCurrentComponent()
text = model.Text

#text = uno.getComponentContext().ServiceManager.createInstanceWithContext( "com.sun.star.bridge.UnoUrlResolver", uno.getComponentContext() ).resolve( "uno:socket,host=lostlcahost,port=2002;urp;StarOffice.ComponentContext").ServiceManager.createInstanceWithContext( "com.sun.star.frame.Desktop",uno.getComponentContext().ServiceManager.createInstanceWithContext( "com.sun.star.bridge.UnoUrlResolver", uno.getComponentContext() ).resolve( "uno:socket,host=lostlcahost,port=2002;urp;StarOffice.ComponentContext")).getCurrentComponent().Text
cursor = text.createTextCursor()

text.insertString(cursor, "Hello World", 0)
#ctx.ServiceManager


