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
                            <sld:ColorMapEntry color="#FFFFFF" opacity="1.0" quantity="0.000000001" label="0"/>                         
                            <sld:ColorMapEntry color="#00600C" opacity="1.0" quantity="500000" label="500,000"/>                          
                            <sld:ColorMapEntry color="#8AB500" opacity="1.0" quantity="1000000" label="1,000,000"/>                          
                            <sld:ColorMapEntry color="#FFE500" opacity="1.0" quantity="1500000" label="1,500,000"/>
                            <sld:ColorMapEntry color="#FFA500" opacity="1.0" quantity="2000000" label="2,000,000"/>                          
                            <sld:ColorMapEntry color="#FF6E00" opacity="1.0" quantity="2500000" label="2,500,000"/>                          
                            <sld:ColorMapEntry color="#FF2100" opacity="1.0" quantity="3000000" label="3,000,000"/> 
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>