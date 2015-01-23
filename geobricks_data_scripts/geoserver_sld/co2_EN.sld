<?xml version="1.0" encoding="UTF-8"?>
<sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>20120812</sld:Name>
            <sld:Title/>
            <sld:FeatureTypeStyle>
                <sld:Name>name</sld:Name>
                <sld:FeatureTypeName>Feature</sld:FeatureTypeName>
                <sld:Rule>
                    <sld:RasterSymbolizer>
                        <sld:Geometry>
                            <ogc:PropertyName>geom</ogc:PropertyName>
                        </sld:Geometry>
                        <sld:ColorMap type="intervals">
                            <sld:ColorMapEntry color="#FFFFFF" opacity="0.00000000001" quantity="0" label="UNITS"/>                      
                            <sld:ColorMapEntry color="#00600C" opacity="1.0" quantity="0.000000001" label="0"/>                          
                            <sld:ColorMapEntry color="#8AB500" opacity="1.0" quantity="400" label="400"/>                          
                            <sld:ColorMapEntry color="#D6E500" opacity="1.0" quantity="800" label="800"/>                          
                            <sld:ColorMapEntry color="#FFE500" opacity="1.0" quantity="1200" label="1,200"/>
                            <sld:ColorMapEntry color="#FFA500" opacity="1.0" quantity="1600" label="1,600"/>                                                   
                            <sld:ColorMapEntry color="#FF2100" opacity="1.0" quantity="2000" label="2,000"/> 
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>