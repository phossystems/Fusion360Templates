#Author-Nico Schlueter
#Description-An example of none feature-based modeling using Python for speed and freedom

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    try:
        # Some nice variables you frequently need
        app = adsk.core.Application.get()
        des = app.activeProduct
        root = des.rootComponent
        bodies = root.bRepBodies










# ============================== Entering direct design mode ==============================


        # Document Design Type ( Parametric or Direct )
        # 0 = Direct, 1 = Parametric
        # Setting this is possible, but not recommended,
        # since Base feature offer the same benifit without affecting the rest of the document
        designType = des.designType
        
        

        # Creating a base feature is the best option for doing direct modeling in an otherwise parametric design
        # Needs to be created, started and finished afterwards
        baseFeature = root.features.baseFeatures.add()
        baseFeature.startEdit() 










# ============================== Creating Primitves ==============================


        # The temporaryBRep manager is a tool for creating 3d geometry without the use of features
        # The word temporary referrs to the geometry being created being virtual, but It can easily be converted to actual geometry
        tbm = adsk.fusion.TemporaryBRepManager.get()

        #Array to keep track of TempBRepBodies
        tempBRepBodies = []



        
        # Creates a oriented Cuboid volume representation
        # Point3D  : Center
        # Vector3D : Axis1
        # Vector3D : Axis2
        # double   : length
        # double   : width
        # double   : height
        obb = adsk.core.OrientedBoundingBox3D.create( adsk.core.Point3D.create(0,0,1),
                                                      adsk.core.Vector3D.create(1,0,0),
                                                      adsk.core.Vector3D.create(0,1,0),
                                                      4, 2, 2 )
        box = tbm.createBox(obb)
        tempBRepBodies.append(box)




        # Creates a oriented Cuboid volume representation
        # Point3D  : Center
        # Vector3D : Axis1
        # Vector3D : Axis2
        # double   : length
        # double   : width
        # double   : height
        obb = adsk.core.OrientedBoundingBox3D.create( adsk.core.Point3D.create(0,5, 2),
                                                      adsk.core.Vector3D.create(0.5, -0.707107 ,0.5),
                                                      adsk.core.Vector3D.create(0.707107, 0, -0.707107),
                                                      3, 3, 3 )
        box = tbm.createBox(obb)
        tempBRepBodies.append(box)




        # Creates a Cylinder or cone by two points and two radii
        # Point3D : Start Point
        # double  : Start Radius
        # Point3D : End Point
        # double  : End Radius
        cylinder = tbm.createCylinderOrCone(adsk.core.Point3D.create(5, 0, 0),
                                            2,
                                            adsk.core.Point3D.create(5, 0, 2),
                                            2)
        tempBRepBodies.append(cylinder)




        # Creates a Cylinder or cone by two points and two radii
        # Point3D : Start Point
        # double  : Start Radius
        # Point3D : End Point
        # double  : End Radius
        cylinder = tbm.createCylinderOrCone(adsk.core.Point3D.create(5, 5, 0),
                                            2,
                                            adsk.core.Point3D.create(5, 5, 4),
                                            0)
        tempBRepBodies.append(cylinder)




        # Creates a Cylinder or cone by two points and two radii
        # Point3D : Start Point
        # double  : Start Radius
        # Point3D : End Point
        # double  : End Radius
        cylinder = tbm.createCylinderOrCone(adsk.core.Point3D.create(5, 10, 0),
                                            2,
                                            adsk.core.Point3D.create(5, 10, 2),
                                            1)
        tempBRepBodies.append(cylinder)




        # Creates an elliptical Cylinder or cone by two points, three radii and a direction
        # Point3D  : Start Point
        # double   : Start Major Radius
        # double   : Start Minor Radius
        # Point3D  : End Point
        # double   : End Major Radius
        # Vector3D : Major Radius Direction
        elCylinder = tbm.createEllipticalCylinderOrCone(adsk.core.Point3D.create(10, 0, 0),
                                                        2,
                                                        1.5,
                                                        adsk.core.Point3D.create(10, 0, 2),
                                                        2,
                                                        adsk.core.Vector3D.create(2, 1, 0) )
        tempBRepBodies.append(elCylinder)




        # Creates an elliptical Cylinder or cone by two points, three radii and a direction
        # Point3D  : Start Point
        # double   : Start Major Radius
        # double   : Start Minor Radius
        # Point3D  : End Point
        # double   : End Major Radius
        # Vector3D : Major Radius Direction
        elCylinder = tbm.createEllipticalCylinderOrCone(adsk.core.Point3D.create(10, 5, 0),
                                                        2,
                                                        1.5,
                                                        adsk.core.Point3D.create(10, 5, 4),
                                                        0,
                                                        adsk.core.Vector3D.create(2, -1, 0) )
        tempBRepBodies.append(elCylinder)




        # Creates an elliptical Cylinder or cone by two points, three radii and a direction
        # Point3D  : Start Point
        # double   : Start Major Radius
        # double   : Start Minor Radius
        # Point3D  : End Point
        # double   : End Major Radius
        # Vector3D : Major Radius Direction
        elCylinder = tbm.createEllipticalCylinderOrCone(adsk.core.Point3D.create(10, 10, 0),
                                                        2,
                                                        1.5,
                                                        adsk.core.Point3D.create(10, 10, 2),
                                                        1,
                                                        adsk.core.Vector3D.create(2, -1, 0) )
        tempBRepBodies.append(elCylinder)
        



        # Creates a sphere by point and radius
        # Point3D : Center Point
        # double  : radius
        sphere = tbm.createSphere(adsk.core.Point3D.create(15, 0, 1.5),
                                  2)
        tempBRepBodies.append(sphere)




        # Creates a Torus by point, axis and radii
        # Point3D  : Center Point
        # Vector3D : Axis
        # double   : Major Radius
        # double   : Minor Radius
        torus = tbm.createTorus(adsk.core.Point3D.create(20, -5, 0.75),
                                adsk.core.Vector3D.create(0, 0, 1),
                                1.5,
                                0.75)
        tempBRepBodies.append(torus)










# ============================== Boolean Operations ==============================


        cylinder1 = tbm.createCylinderOrCone(adsk.core.Point3D.create(25, 0, 0),
                                             2,
                                             adsk.core.Point3D.create(25, 0, 2),
                                             2)

        cylinder2 = tbm.createCylinderOrCone(adsk.core.Point3D.create(27, 0, -1),
                                             1,
                                             adsk.core.Point3D.create(27, 0, 3),
                                             1)

        # Performs boolean operation on body
        # BRepBody : Body to modify
        # BRepBody : Tool Body
        # int      : Operation type ( 0:Difference, 1:Intersection, 2:Union )
        tbm.booleanOperation(cylinder1, cylinder2, 0)
        tempBRepBodies.append(cylinder1)




        cylinder1 = tbm.createCylinderOrCone(adsk.core.Point3D.create(25, 5, 0),
                                             2,
                                             adsk.core.Point3D.create(25, 5, 2),
                                             2)

        cylinder2 = tbm.createCylinderOrCone(adsk.core.Point3D.create(27, 5, -1),
                                             1,
                                             adsk.core.Point3D.create(27, 5, 3),
                                             1)

        # Performs boolean operation on body
        # BRepBody : Body to modify
        # BRepBody : Tool Body
        # int      : Operation type ( 0:Difference, 1:Intersection, 2:Union )
        tbm.booleanOperation(cylinder1, cylinder2, 1)
        tempBRepBodies.append(cylinder1)




        cylinder1 = tbm.createCylinderOrCone(adsk.core.Point3D.create(25, 10, 0),
                                             2,
                                             adsk.core.Point3D.create(25, 10, 2),
                                             2)

        cylinder2 = tbm.createCylinderOrCone(adsk.core.Point3D.create(27, 10, -1),
                                             1,
                                             adsk.core.Point3D.create(27, 10, 3),
                                             1)

        # Performs boolean operation on body
        # BRepBody : Body to modify
        # BRepBody : Tool Body
        # int      : Operation type ( 0:Difference, 1:Intersection, 2:Union )
        tbm.booleanOperation(cylinder1, cylinder2, 2)
        tempBRepBodies.append(cylinder1)




        obb = adsk.core.OrientedBoundingBox3D.create( adsk.core.Point3D.create(25,15,2),
                                                      adsk.core.Vector3D.create(1,0,0),
                                                      adsk.core.Vector3D.create(0,1,0),
                                                      4, 4, 4 )
        box = tbm.createBox(obb)

        cylinder1 = tbm.createCylinderOrCone(adsk.core.Point3D.create(25, 15, 0),
                                             1.5,
                                             adsk.core.Point3D.create(25, 15, 4),
                                             1.5)

        cylinder2 = tbm.createCylinderOrCone(adsk.core.Point3D.create(25, 13, 2),
                                             1.5,
                                             adsk.core.Point3D.create(25, 17, 2),
                                             1.5)

        cylinder3 = tbm.createCylinderOrCone(adsk.core.Point3D.create(23, 15, 2),
                                             1.5,
                                             adsk.core.Point3D.create(27, 15, 2),
                                             1.5)

        tbm.booleanOperation(box, cylinder1, 0)
        tbm.booleanOperation(box, cylinder2, 0)
        tbm.booleanOperation(box, cylinder3, 0)

        tempBRepBodies.append(box)










# ============================== Surface Creation ==============================

        
        # Creates a object representing a circle in 3D space by a point, axis and radius
        # Point3D  : Center Point
        # Vector3D : Axis
        # Double   : Radius
        circle = adsk.core.Circle3D.createByCenter(adsk.core.Point3D.create(30, 0, 0),
                                                   adsk.core.Vector3D.create(0,0,1),
                                                   2)

        # Creates BRep wire object(s), representing edges in 3D space from an array of 3Dcurves
        # Curve3D[] : Curves
        wireBody, _ = tbm.createWireFromCurves([circle])

        # Creates a planar face from an array of Wires.
        face = tbm.createFaceFromPlanarWires([wireBody])

        tempBRepBodies.append(face)




        # Creates a object representing a circle in 3D space by a point, axis and radius
        # Point3D  : Center Point
        # Vector3D : Axis
        # Double   : Radius
        circle1 = adsk.core.Circle3D.createByCenter(adsk.core.Point3D.create(30, 5, 0),
                                                   adsk.core.Vector3D.create(0,0,1),
                                                   2)

        circle2 = adsk.core.Circle3D.createByCenter(adsk.core.Point3D.create(30.5, 5, 0),
                                                   adsk.core.Vector3D.create(0,0,1),
                                                   1)

        # Creates BRep wire object(s), representing edges in 3D space from an array of 3Dcurves
        # Curve3D[] : Curves
        wireBody, _ = tbm.createWireFromCurves([circle1, circle2])

        # Creates a planar face from an array of Wires.
        face = tbm.createFaceFromPlanarWires([wireBody])

        tempBRepBodies.append(face)




        #Creates an object representing a line segemnt in 3D space by two points
        line1 = adsk.core.Line3D.create(adsk.core.Point3D.create(28, 8, 0),
                                        adsk.core.Point3D.create(32, 8, 0))
        line2 = adsk.core.Line3D.create(adsk.core.Point3D.create(32, 8, 0),
                                        adsk.core.Point3D.create(32, 12, 0))
        line3 = adsk.core.Line3D.create(adsk.core.Point3D.create(32, 12, 0),
                                        adsk.core.Point3D.create(28, 12, 0))
        line4 = adsk.core.Line3D.create(adsk.core.Point3D.create(28, 12, 0),
                                        adsk.core.Point3D.create(28, 8, 0))

        # Creates BRep wire object(s), representing edges in 3D space from an array of 3Dcurves
        # Curve3D[] : Curves
        wireBody, _ = tbm.createWireFromCurves([line1, line2, line3, line4])

        # Creates a planar face from an array of Wires.
        face = tbm.createFaceFromPlanarWires([wireBody])

        tempBRepBodies.append(face)




        # Creates a object representing a circle in 3D space by a point, axis and radius
        # Point3D  : Center Point
        # Vector3D : Axis
        # Double   : Radius
        circle1 = adsk.core.Circle3D.createByCenter(adsk.core.Point3D.create(35, 0, 0),
                                                   adsk.core.Vector3D.create(0,0,1),
                                                   2)

        circle2 = adsk.core.Circle3D.createByCenter(adsk.core.Point3D.create(35, 0, 2),
                                                   adsk.core.Vector3D.create(0,0,1),
                                                   2)

        # Creates BRep wire object(s), representing edges in 3D space from an array of 3Dcurves
        # Curve3D[] : Curves
        wireBody1, _ = tbm.createWireFromCurves([circle1])

        wireBody2, _ = tbm.createWireFromCurves([circle2])

        # Creates a ruled surface (e.g. Straight Loft) of two wires
        # Warning! createWireFromCurve does not actually create a wire but a BRepBody
        # BRepWire : Wire1
        # BRepWire : Wire2
        surface = tbm.createRuledSurface(wireBody1.wires.item(0), wireBody2.wires.item(0))

        tempBRepBodies.append(surface)




        #Creates an object representing a line segemnt in 3D space by two points
        line1 = adsk.core.Line3D.create(adsk.core.Point3D.create(33, 3, 0),
                                        adsk.core.Point3D.create(37, 3, 0))
        line2 = adsk.core.Line3D.create(adsk.core.Point3D.create(37, 3, 0),
                                        adsk.core.Point3D.create(37, 7, 0))
        line3 = adsk.core.Line3D.create(adsk.core.Point3D.create(37, 7, 0),
                                        adsk.core.Point3D.create(33, 7, 0))
        line4 = adsk.core.Line3D.create(adsk.core.Point3D.create(33, 7, 0),
                                        adsk.core.Point3D.create(33, 3, 0))

        line5 = adsk.core.Line3D.create(adsk.core.Point3D.create(33, 3, 2),
                                        adsk.core.Point3D.create(37, 3, 2))
        line6 = adsk.core.Line3D.create(adsk.core.Point3D.create(37, 3, 2),
                                        adsk.core.Point3D.create(37, 7, 2))
        line7 = adsk.core.Line3D.create(adsk.core.Point3D.create(37, 7, 2),
                                        adsk.core.Point3D.create(33, 7, 2))
        line8 = adsk.core.Line3D.create(adsk.core.Point3D.create(33, 7, 2),
                                        adsk.core.Point3D.create(33, 3, 2))

        # Creates BRep wire object(s), representing edges in 3D space from an array of 3Dcurves
        # Curve3D[] : Curves
        wireBody1, _ = tbm.createWireFromCurves([line1, line2, line3, line4])

        wireBody2, _ = tbm.createWireFromCurves([line5, line6, line7, line8])

        # Creates a ruled surface (e.g. Straight Loft) of two wires
        # Warning! createWireFromCurve does not actually create a wire but a BRepBody
        # BRepWire : Wire1
        # BRepWire : Wire2
        surface = tbm.createRuledSurface(wireBody1.wires.item(0), wireBody2.wires.item(0))

        tempBRepBodies.append(surface)




        #Creates an object representing a line segemnt in 3D space by two points
        line1 = adsk.core.Line3D.create(adsk.core.Point3D.create(33, 8, 0),
                                        adsk.core.Point3D.create(37, 8, 0))
        line2 = adsk.core.Line3D.create(adsk.core.Point3D.create(37, 8, 0),
                                        adsk.core.Point3D.create(37, 12, 0))
        line3 = adsk.core.Line3D.create(adsk.core.Point3D.create(37, 12, 0),
                                        adsk.core.Point3D.create(33, 12, 0))
        line4 = adsk.core.Line3D.create(adsk.core.Point3D.create(33, 12, 0),
                                        adsk.core.Point3D.create(33, 8, 0))

        circle1 = adsk.core.Circle3D.createByCenter(adsk.core.Point3D.create(35, 10, 2),
                                                   adsk.core.Vector3D.create(0,0,1),
                                                   1)

        # Creates BRep wire object(s), representing edges in 3D space from an array of 3Dcurves
        # Curve3D[] : Curves
        wireBody1, _ = tbm.createWireFromCurves([line1, line2, line3, line4])

        wireBody2, _ = tbm.createWireFromCurves([circle1])

        # Creates a ruled surface (e.g. Straight Loft) of two wires
        # Warning! createWireFromCurve does not actually create a wire but a BRepBody
        # BRepWire : Wire1
        # BRepWire : Wire2
        surface = tbm.createRuledSurface(wireBody1.wires.item(0), wireBody2.wires.item(0))

        tempBRepBodies.append(surface)




        #Adds all temporary BRepBodies to the real (non Temporary) Bodies
        for b in tempBRepBodies:
            bodies.add(b, baseFeature)










# ============================== Surface Creation ==============================


        # Creates an object representing a Plane in 3D space by point and vector
        # Point3D  : center Point
        # Vector3D : Normal Vector
        plane = adsk.core.Plane.create(adsk.core.Point3D.create(40,0, 1),
                                       adsk.core.Vector3D.create(1,-3,5))

        # Creates an object responsible for passing all required data to create a construction plane
        planeInput = root.constructionPlanes.createInput()

        # Sets the plane input by plane
        planeInput.setByPlane(plane)

        # Adds plain input to construction planes
        root.constructionPlanes.add(planeInput)




        # Creates an Object representing an infinite line by a point and a Vector
        # Point3D  : Starting point
        # Vector3D : Direction
        line = adsk.core.InfiniteLine3D.create(adsk.core.Point3D.create(39, 4, -1),
                                        adsk.core.Vector3D.create(20,20,40))

        # Creates an object responsible for passing all required data to create a construction axis
        axisInput = root.constructionAxes.createInput()

        # Sets the axis by Infinite line
        axisInput.setByLine(line)

        # Adds the axis to constructon axes
        root.constructionAxes.add(axisInput)




        point = adsk.core.Point3D.create(40, 10, 1)

        # Creates an object responsible for passing all required data to create a construction point
        pointInput = root.constructionPoints.createInput()

        # Sets the point by point
        pointInput.setByPoint(point)

        # Adds the point to construction Points
        root.constructionPoints.add(pointInput)




        # Finishes the base feature
        baseFeature.finishEdit()
    except:
            print(traceback.format_exc())