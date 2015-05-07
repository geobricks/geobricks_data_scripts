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
                        <sld:ColorMap type="ramp">
                            <sld:ColorMapEntry color="#ffffff" opacity="0.00000000001" quantity="0" label="Burned Areas"/>
                            <sld:ColorMapEntry color="#ffffb2" opacity="1.0" quantity="0.00001" label="Low"/>                         
                            <sld:ColorMapEntry color="#fecc5c" opacity="1.0" quantity="30" label="Low-Average"/>                          
                            <sld:ColorMapEntry color="#fd8d3c" opacity="1.0" quantity="67" label="Average"/>                          
                            <sld:ColorMapEntry color="#f03b20" opacity="1.0" quantity="5000" label="High-Average"/>                          
                            <sld:ColorMapEntry color="#bd0026" opacity="1.0" quantity="11999" label="High"/>                          
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>