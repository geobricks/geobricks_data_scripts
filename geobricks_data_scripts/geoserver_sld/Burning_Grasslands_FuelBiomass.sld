<?xml version="1.0" ?>
<sld:StyledLayerDescriptor version="1.0.0" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>Grasslands_FuelBiomass</sld:Name>
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
			    <sld:ColorMapEntry color="#ffffff" label="T (Dry Matter)/Ha" opacity="0.00000001" quantity="0.00000001"/>
                            <sld:ColorMapEntry color="#ffffff" label="No Data" opacity="0.00000001" quantity="0.00000001"/>
                            <sld:ColorMapEntry color="#ffffbe" label="Grassland: 4.1" opacity="1.0" quantity="4.1"/>
                            <sld:ColorMapEntry color="#aaff00" label="Tropical\Subtropical grassland: 5.2" opacity="1.0" quantity="5.2"/>
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>
