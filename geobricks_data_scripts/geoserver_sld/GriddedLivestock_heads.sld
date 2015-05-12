<?xml version="1.0" ?>
<sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>GriddedLivestock_heads</sld:Name>
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
                            <sld:ColorMapEntry color="#ffffff" label="Heads" opacity="0.0000001" quantity="0.0000001"/>
                            <sld:ColorMapEntry color="#ffffff" label="No Data " opacity="0.0000001" quantity="0.0000001"/>
                            <sld:ColorMapEntry color="#92c800" label="&gt; 0 - 50" opacity="1.0" quantity="50"/>
                            <sld:ColorMapEntry color="#ffff00" label="50 - 100" opacity="1.0" quantity="100"/>
                            <sld:ColorMapEntry color="#ff8400" label="100 - 150" opacity="1.0" quantity="150"/>
                            <sld:ColorMapEntry color="#ff2600" label="&gt; 150" opacity="1.0" quantity="99999"/>
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>
