<?xml version="1.0" ?>
<sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>GFED4_BurnedArea</sld:Name>
            <sld:Title/>
            <sld:FeatureTypeStyle>
                <sld:Name/>
                <sld:Rule>
                    <sld:RasterSymbolizer>
                        <sld:Geometry>
                            <ogc:PropertyName>grid</ogc:PropertyName>
                        </sld:Geometry>
                        <sld:Opacity>1</sld:Opacity>
                        <sld:ColorMap type="intervals">
                            <sld:ColorMapEntry color="#ffffff" label="ha (Hectares)" opacity="0.0000001" quantity="0.0000001"/>
                            <sld:ColorMapEntry color="#ffffff" label="No Data" opacity="0.0000001" quantity="0.0000001"/>
                            <sld:ColorMapEntry color="#ffffb2" label="Low (0 - 100)" opacity="1.0" quantity="100"/>
                            <sld:ColorMapEntry color="#fecc5c" label="Low - Average (100 - 1,000)" opacity="1.0" quantity="1000"/>
                            <sld:ColorMapEntry color="#fd8d3c" label="Average (1,000 - 5,000)" opacity="1.0" quantity="5000"/>
                            <sld:ColorMapEntry color="#f03b20" label="High - Average (5,000 - 10,000)" opacity="1.0" quantity="10000"/>
                            <sld:ColorMapEntry color="#bd0026" label="High (&gt; 10,000)" opacity="1.0" quantity="100000"/>
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>
