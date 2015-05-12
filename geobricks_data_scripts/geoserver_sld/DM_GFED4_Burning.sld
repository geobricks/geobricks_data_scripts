<?xml version="1.0" ?>
<sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>DM_GFED4_Burning</sld:Name>
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
			    <sld:ColorMapEntry color="#ffffff" label="T (Tonnes)" opacity="0.0000001" quantity="0.0000001"/>
                            <sld:ColorMapEntry color="#ffffff" label="No Data" opacity="0.0000001" quantity="0.0000001"/>
                            <sld:ColorMapEntry color="#38a800" label=">0 - 50,000" opacity="1.0" quantity="0.1"/>
                            <sld:ColorMapEntry color="#6fc400" label="50,000 - 250,000" opacity="1.0" quantity="50000"/>
                            <sld:ColorMapEntry color="#b0e000" label="250,000 - 500,000" opacity="1.0" quantity="250000"/>
                            <sld:ColorMapEntry color="#ffff00" label="500,000 - 750,000" opacity="1.0" quantity="500000"/>
                            <sld:ColorMapEntry color="#ffaa00" label="750,000 - 1,000,000" opacity="1.0" quantity="750000"/>
                            <sld:ColorMapEntry color="#ff5500" label="1,000,000 - 2,000,000" opacity="1.0" quantity="1e+06"/>
                            <sld:ColorMapEntry color="#ff0000" label="2,000,000 - 3,000,000" opacity="1.0" quantity="2e+06"/>
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>
